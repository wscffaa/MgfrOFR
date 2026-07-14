import torch
import torch.nn as nn
import torch.nn.functional as F

from basicsr.utils.registry import LOSS_REGISTRY


@LOSS_REGISTRY.register()
class BranchDiversityLoss(nn.Module):
    """Branch decorrelation regularizer (RATR-free diversity alternative).

    Drop-in replacement for ``ratr_opt`` that addresses Reviewer 2's request for
    an alternative diversity-regularization loss. Instead of ranking-aware
    triplets, it enforces complementary branches directly: per timestep, each
    branch descriptor is L2-normalized over its channel dimension, a cross-branch
    Gram matrix is formed, and the squared off-diagonal entries (cross-branch
    cosine similarities) are penalized. The loss is 0 when branches are mutually
    orthogonal and grows toward 1 as branches become collinear (redundant).

    Shares the RATRLoss public signature ``forward(branch_feats, sequence_length)``
    so it can be swapped via config without touching the training model.
    """

    def __init__(self, loss_weight: float = 0.1, eps: float = 1e-8):
        super().__init__()
        self.loss_weight = loss_weight
        self.eps = eps

    def forward(self, branch_feats: torch.Tensor, sequence_length: int | None = None) -> torch.Tensor:
        if branch_feats is None:
            raise ValueError('branch_feats must not be None when BranchDiversityLoss is enabled.')

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

        # A single branch has no cross-branch pairs to decorrelate.
        if g < 2:
            return branch_feats.new_zeros(())

        normalized = F.normalize(branch_feats.float(), dim=-1, eps=self.eps)
        gram = normalized @ normalized.transpose(-2, -1)  # (b, t, g, g), diagonal == 1

        off_diag = 1.0 - torch.eye(g, device=gram.device, dtype=gram.dtype)
        penalty = (gram.pow(2) * off_diag).sum(dim=(-2, -1)) / (g * (g - 1))
        total = penalty.mean()
        return total * self.loss_weight
