from itertools import combinations

import torch
import torch.nn as nn
import torch.nn.functional as F

from basicsr.utils.registry import LOSS_REGISTRY


@LOSS_REGISTRY.register()
class RATRLoss(nn.Module):
    """Ranking-aware triplet regularization adapted to video frames."""

    def __init__(
        self,
        tau: float = 0.1,
        intra_weight: float = 1.0,
        inter_weight: float = 0.5,
        loss_weight: float = 0.1,
    ):
        super().__init__()
        self.tau = tau
        self.intra_weight = intra_weight
        self.inter_weight = inter_weight
        self.loss_weight = loss_weight

    def _d_ktau(self, x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
        if x.numel() < 2 or y.numel() < 2:
            return x.new_zeros(())

        tau = max(float(self.tau), 1e-6)
        diff_x = torch.tanh((x.unsqueeze(0) - x.unsqueeze(1)) / tau)
        diff_y = torch.tanh((y.unsqueeze(0) - y.unsqueeze(1)) / tau)
        mask = torch.triu(torch.ones_like(diff_x, dtype=torch.bool), diagonal=1)
        return (diff_x[mask] * diff_y[mask]).mean()

    @staticmethod
    def _build_negative_sequence(
        flat_feats: torch.Tensor,
        anchor_idx: int,
        branch_idx: int,
        video_ids: torch.Tensor,
        frame_ids: torch.Tensor,
    ) -> torch.Tensor | None:
        anchor_feat = flat_feats[anchor_idx, branch_idx]
        anchor_video = video_ids[anchor_idx]
        anchor_frame = frame_ids[anchor_idx]

        negatives = []

        same_video_distant = (video_ids == anchor_video) & (torch.abs(frame_ids - anchor_frame) > 1)
        if same_video_distant.any():
            negatives.append(F.linear(anchor_feat.unsqueeze(0), flat_feats[same_video_distant, branch_idx]).squeeze(0))

        for other_video in video_ids.unique(sorted=True):
            if other_video == anchor_video:
                continue
            other_mask = video_ids == other_video
            if not other_mask.any():
                continue
            centroid = flat_feats[other_mask, branch_idx].mean(dim=0, keepdim=True)
            negatives.append(F.linear(anchor_feat.unsqueeze(0), centroid).reshape(-1))

        if not negatives:
            return None

        return torch.cat(negatives, dim=0)

    def forward(self, branch_feats: torch.Tensor, sequence_length: int | None = None) -> torch.Tensor:
        if branch_feats is None:
            raise ValueError('branch_feats must not be None when RATRLoss is enabled.')

        if branch_feats.dim() == 4:
            b, t, g, d = branch_feats.shape
        elif branch_feats.dim() == 3:
            bt, g, d = branch_feats.shape
            if sequence_length is None:
                b, t = 1, bt
            else:
                if bt % sequence_length != 0:
                    raise ValueError(f'branch_feats length {bt} is not divisible by sequence_length {sequence_length}.')
                b = bt // sequence_length
                t = sequence_length
            branch_feats = branch_feats.view(b, t, g, d)
        else:
            raise ValueError(f'Unsupported branch_feats shape: {tuple(branch_feats.shape)}')

        if g < 2:
            return branch_feats.new_zeros(())

        branch_feats = F.normalize(branch_feats.float(), dim=-1)
        flat_feats = branch_feats.view(b * t, g, d)
        video_ids = torch.arange(b, device=branch_feats.device).unsqueeze(1).expand(b, t).reshape(-1)
        frame_ids = torch.arange(t, device=branch_feats.device).unsqueeze(0).expand(b, t).reshape(-1)

        sim_mats = []
        for branch_idx in range(g):
            sim_mats.append(flat_feats[:, branch_idx] @ flat_feats[:, branch_idx].transpose(0, 1))

        branch_pairs = list(combinations(range(g), 2))
        if not branch_pairs:
            return branch_feats.new_zeros(())

        intra_terms = []
        inter_terms = []

        for anchor_idx in range(b * t):
            anchor_video = video_ids[anchor_idx]
            anchor_frame = frame_ids[anchor_idx]
            positive_mask = (video_ids == anchor_video) & (torch.abs(frame_ids - anchor_frame) == 1)

            for left_branch, right_branch in branch_pairs:
                if positive_mask.any():
                    left_positive = sim_mats[left_branch][anchor_idx, positive_mask]
                    right_positive = sim_mats[right_branch][anchor_idx, positive_mask]
                    intra_terms.append(self._d_ktau(left_positive, right_positive))

                left_negative = self._build_negative_sequence(
                    flat_feats, anchor_idx, left_branch, video_ids, frame_ids
                )
                right_negative = self._build_negative_sequence(
                    flat_feats, anchor_idx, right_branch, video_ids, frame_ids
                )
                if left_negative is not None and right_negative is not None:
                    inter_terms.append(self._d_ktau(left_negative, right_negative))

        zero = branch_feats.new_zeros(())
        intra_loss = torch.stack(intra_terms).mean() if intra_terms else zero
        inter_loss = torch.stack(inter_terms).mean() if inter_terms else zero
        total = self.intra_weight * intra_loss + self.inter_weight * inter_loss
        return total * self.loss_weight
