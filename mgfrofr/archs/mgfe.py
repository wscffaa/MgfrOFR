import torch
import torch.nn as nn
from torch.utils.checkpoint import checkpoint as grad_checkpoint


class LinearTokenBlock(nn.Module):
    """Linear-complexity token block with shared global context."""

    def __init__(self, dim: int, mlp_ratio: float = 2.0):
        super().__init__()
        hidden_dim = max(dim, int(dim * mlp_ratio))
        self.norm1 = nn.LayerNorm(dim)
        self.token_proj = nn.Linear(dim, dim)
        self.context_proj = nn.Linear(dim, dim)
        self.norm2 = nn.LayerNorm(dim)
        self.mlp = nn.Sequential(
            nn.Linear(dim, hidden_dim),
            nn.GELU(),
            nn.Linear(hidden_dim, dim),
        )

    def forward(self, tokens: torch.Tensor) -> torch.Tensor:
        residual = tokens
        tokens = self.norm1(tokens)
        global_context = tokens.mean(dim=1, keepdim=True)
        tokens = residual + self.token_proj(tokens) + self.context_proj(global_context)
        tokens = tokens + self.mlp(self.norm2(tokens))
        return tokens


class MGFE(nn.Module):
    """Multi-granularity feature extractor for OFR feature maps."""

    def __init__(
        self,
        in_channels: int,
        num_tokens: int = 12,
        num_branches: int = 3,
        token_fusion: str = 'max',
        use_checkpoint: bool = False,
    ):
        super().__init__()
        self.in_channels = in_channels
        self.num_tokens = num_tokens
        self.num_branches = num_branches
        self.token_fusion = token_fusion.lower()
        self.use_checkpoint = use_checkpoint

        if self.token_fusion not in {'max', 'avg', 'mean', 'min'}:
            raise ValueError(f'Unsupported token fusion: {token_fusion}')

        self.restoration_tokens = nn.Parameter(torch.zeros(1, num_tokens, in_channels))
        nn.init.trunc_normal_(self.restoration_tokens, std=0.02)

        self.branch_blocks = nn.ModuleList()
        for _ in range(num_branches):
            self.branch_blocks.append(
                nn.ModuleList(
                    [
                        LinearTokenBlock(in_channels),
                        LinearTokenBlock(in_channels),
                    ]
                )
            )

        hidden_dim = max(in_channels, in_channels * 2)
        self.recalibrate = nn.Sequential(
            nn.LayerNorm(in_channels),
            nn.Linear(in_channels, hidden_dim),
            nn.GELU(),
            nn.Linear(hidden_dim, in_channels * 2),
        )

    def _fuse_restoration_tokens(self, tokens: torch.Tensor, rate: int) -> torch.Tensor:
        b, m, c = tokens.shape
        if m == 0:
            return tokens

        pad = (-m) % rate
        if pad:
            tokens = torch.cat([tokens, tokens[:, -1:, :].expand(-1, pad, -1)], dim=1)

        tokens = tokens.view(b, -1, rate, c)
        if self.token_fusion == 'max':
            return tokens.max(dim=2).values
        if self.token_fusion in {'avg', 'mean'}:
            return tokens.mean(dim=2)
        return tokens.min(dim=2).values

    @staticmethod
    def _evenly_insert_tokens(
        image_tokens: torch.Tensor,
        restoration_tokens: torch.Tensor,
    ) -> tuple[torch.Tensor, list[int]]:
        num_image = image_tokens.size(1)
        num_restoration = restoration_tokens.size(1)
        if num_restoration == 0:
            return image_tokens, []

        chunk_count = num_restoration + 1
        base, extra = divmod(num_image, chunk_count)

        parts = []
        positions: list[int] = []
        image_cursor = 0
        out_cursor = 0

        for chunk_idx in range(chunk_count):
            chunk_size = base + (1 if chunk_idx < extra else 0)
            if chunk_size > 0:
                parts.append(image_tokens[:, image_cursor:image_cursor + chunk_size, :])
                image_cursor += chunk_size
                out_cursor += chunk_size
            if chunk_idx < num_restoration:
                parts.append(restoration_tokens[:, chunk_idx:chunk_idx + 1, :])
                positions.append(out_cursor)
                out_cursor += 1

        return torch.cat(parts, dim=1), positions

    def _compute_core(self, feat_prop: torch.Tensor) -> dict[str, torch.Tensor]:
        """Shared computation for forward() and forward_with_intermediates()."""
        b, c, h, w = feat_prop.shape
        image_tokens = feat_prop.flatten(2).transpose(1, 2)
        restoration_tokens = self.restoration_tokens.expand(b, -1, -1)

        branch_feats = []
        all_token_positions: list[list[int]] = []
        per_branch_token_energy: list[torch.Tensor] = []

        for branch_idx, blocks in enumerate(self.branch_blocks):
            fusion_rate = 2 ** branch_idx
            fused_tokens = self._fuse_restoration_tokens(restoration_tokens, fusion_rate)
            branch_tokens, restoration_positions = self._evenly_insert_tokens(image_tokens, fused_tokens)
            all_token_positions.append(restoration_positions)

            for block in blocks:
                if self.use_checkpoint and branch_tokens.requires_grad:
                    branch_tokens = grad_checkpoint(block, branch_tokens, use_reentrant=False)
                else:
                    branch_tokens = block(branch_tokens)

            if restoration_positions:
                index = torch.tensor(restoration_positions, device=branch_tokens.device, dtype=torch.long)
                selected = branch_tokens.index_select(1, index)
                branch_descriptor = selected.mean(dim=1)
                per_branch_token_energy.append(selected.abs().mean(dim=-1))
            else:
                branch_descriptor = branch_tokens.mean(dim=1)
                per_branch_token_energy.append(branch_tokens.abs().mean(dim=-1)[:, :1])
            branch_feats.append(branch_descriptor)

        branch_feats = torch.stack(branch_feats, dim=1)
        context = branch_feats.mean(dim=1)
        recalib_out = self.recalibrate(context)
        scale_raw, shift_raw = recalib_out.chunk(2, dim=-1)
        scale = torch.tanh(scale_raw).view(b, c, 1, 1)
        shift = 0.1 * torch.tanh(shift_raw).view(b, c, 1, 1)
        recalibrated = feat_prop * (1.0 + scale) + shift

        return {
            'recalibrated': recalibrated,
            'branch_feats': branch_feats,
            'scale': scale,
            'shift': shift,
            'token_positions': all_token_positions,
            'per_branch_token_energy': per_branch_token_energy,
        }

    def forward(self, feat_prop: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
        core = self._compute_core(feat_prop)
        return core['recalibrated'], core['branch_feats']

    def forward_with_intermediates(self, feat_prop: torch.Tensor) -> dict[str, torch.Tensor]:
        """Forward pass returning all intermediate quantities for visualization.

        Returns dict with keys:
            output: (B, C, H, W) — recalibrated features (same as forward()[0])
            branch_descriptors: (B, num_branches, C)
            branch_similarity: (B, num_branches, num_branches) — pairwise cosine similarity
            scale_map: (B, 1, H, W) — recalibration scale channel-mean spatial map
            shift_map: (B, 1, H, W) — recalibration shift channel-mean spatial map
            recalibration_magnitude: (B, 1, H, W) — L1 delta between input and output
            token_positions: list[list[int]] — per-branch insertion indices
            per_branch_token_energy: list of (B, num_tokens_fused) tensors
        """
        core = self._compute_core(feat_prop)
        b = feat_prop.size(0)
        branch_feats = core['branch_feats']

        normed = torch.nn.functional.normalize(branch_feats, dim=-1)
        branch_sim = torch.bmm(normed, normed.transpose(1, 2))

        return {
            'output': core['recalibrated'],
            'branch_descriptors': branch_feats,
            'branch_similarity': branch_sim,
            'scale_map': core['scale'].mean(dim=1, keepdim=True).expand(b, 1, feat_prop.size(2), feat_prop.size(3)),
            'shift_map': core['shift'].mean(dim=1, keepdim=True).expand(b, 1, feat_prop.size(2), feat_prop.size(3)),
            'recalibration_magnitude': (core['recalibrated'] - feat_prop).abs().mean(dim=1, keepdim=True),
            'token_positions': core['token_positions'],
            'per_branch_token_energy': core['per_branch_token_energy'],
        }
