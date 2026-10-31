"""Token-insertion ablation variant for the Reviewer 2 "insertion strategy" study.

The baseline MGFE interleaves MGFE restoration tokens evenly between image tokens. This
variant prepends them at the head of the token sequence instead. Only the insertion
strategy changes: the ``forward`` / ``forward_with_intermediates`` interfaces and their
return signatures are inherited unchanged from :class:`MGFE`.
"""
import torch

from basicsr.utils.registry import ARCH_REGISTRY

from .mgfe import MGFE
from .mgfrofr_arch import MgfrOFR


class MGFEInsertPrepend(MGFE):
    """MGFE that prepends restoration tokens at the head of the token sequence."""

    @staticmethod
    def _evenly_insert_tokens(
        image_tokens: torch.Tensor,
        restoration_tokens: torch.Tensor,
    ) -> tuple[torch.Tensor, list[int]]:
        # Keep the parent hook name so MGFE._compute_core (self._evenly_insert_tokens)
        # dispatches here through the MRO; the strategy is prepend, not interleave.
        num_restoration = restoration_tokens.size(1)
        if num_restoration == 0:
            return image_tokens, []
        combined = torch.cat([restoration_tokens, image_tokens], dim=1)
        positions = list(range(num_restoration))
        return combined, positions


@ARCH_REGISTRY.register()
class MgfrOFRInsertPrepend(MgfrOFR):
    """MgfrOFR ablation that swaps MGFE for the prepend-insertion MGFE."""

    def __init__(
        self,
        num_feat: int = 16,
        use_mgfe: bool = True,
        mgfe_num_tokens: int = 12,
        mgfe_num_branches: int = 3,
        mgfe_token_fusion: str = 'max',
        use_checkpoint: bool = False,
        **kwargs,
    ):
        super().__init__(
            num_feat=num_feat,
            use_mgfe=use_mgfe,
            mgfe_num_tokens=mgfe_num_tokens,
            mgfe_num_branches=mgfe_num_branches,
            mgfe_token_fusion=mgfe_token_fusion,
            use_checkpoint=use_checkpoint,
            **kwargs,
        )
        self.mgfe = MGFEInsertPrepend(
            in_channels=self.num_feat,
            num_tokens=mgfe_num_tokens,
            num_branches=mgfe_num_branches,
            token_fusion=mgfe_token_fusion,
            use_checkpoint=use_checkpoint,
        )
