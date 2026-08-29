"""Max branch-aggregation ablation for MGFE / MgfrOFR (Reviewer 2).

Reviewer 2 asked for "alternative branch aggregation strategies". The baseline
MGFE fuses its per-branch descriptors with mean aggregation
(``context = branch_feats.mean(dim=1)`` in ``MGFE._compute_core``). This variant
replaces only that step with max aggregation; every other computation, the
returned dict keys, and all public interfaces stay identical to the baseline.
"""

import torch
from torch.utils.checkpoint import checkpoint as grad_checkpoint

from basicsr.utils.registry import ARCH_REGISTRY

from .mgfe import MGFE
from .mgfrofr_arch import MgfrOFR


class MGFEAggMax(MGFE):
    """MGFE variant aggregating branch descriptors with max instead of mean."""

    def _compute_core(self, feat_prop: torch.Tensor) -> dict[str, torch.Tensor]:
        """Identical to MGFE._compute_core except the branch aggregation step."""
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
        # Ablation: max branch aggregation (baseline MGFE uses branch_feats.mean(dim=1)).
        context = branch_feats.max(dim=1).values
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


@ARCH_REGISTRY.register()
class MgfrOFRAggMax(MgfrOFR):
    """MgfrOFR ablation that swaps MGFE for the max-aggregation MGFEAggMax."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        base_mgfe = self.mgfe
        self.mgfe = MGFEAggMax(
            in_channels=base_mgfe.in_channels,
            num_tokens=base_mgfe.num_tokens,
            num_branches=base_mgfe.num_branches,
            token_fusion=base_mgfe.token_fusion,
            use_checkpoint=base_mgfe.use_checkpoint,
        )
