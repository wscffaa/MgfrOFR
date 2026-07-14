import torch

from basicsr.utils.registry import LOSS_REGISTRY

from .ratr_loss import RATRLoss

PEARSON_EPS = 1e-8


@LOSS_REGISTRY.register()
class RATRPearsonLoss(RATRLoss):
    """RATR variant using a differentiable Pearson correlation as the ranking metric.

    Reviewer 2 ("different ranking metrics") asked for an alternative to the soft
    Kendall-tau used by :class:`RATRLoss`. Only the two-sequence correlation hook
    ``_d_ktau`` is overridden; ``__init__`` and the whole forward / intra / inter /
    loss_weight flow are inherited unchanged. ``tau`` is kept for signature
    compatibility but is unused on the Pearson path.
    """

    def _d_ktau(self, x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
        if x.numel() < 2 or y.numel() < 2:
            return x.new_zeros(())

        x_centered = x - x.mean()
        y_centered = y - y.mean()
        numerator = (x_centered * y_centered).sum()
        # eps lives inside each sqrt so the gradient stays finite even when a
        # sequence has zero variance (constant), keeping the metric NaN-safe.
        x_norm = torch.sqrt((x_centered * x_centered).sum() + PEARSON_EPS)
        y_norm = torch.sqrt((y_centered * y_centered).sum() + PEARSON_EPS)
        return numerator / (x_norm * y_norm)
