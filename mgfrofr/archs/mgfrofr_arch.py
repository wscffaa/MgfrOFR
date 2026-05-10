import torch

from basicsr.utils.registry import ARCH_REGISTRY

from basicofr.archs.components import flow_warp
from basicofr.archs.mambaofr_arch import MambaOFRNet
from .mgfe import MGFE


@ARCH_REGISTRY.register()
class MgfrOFR(MambaOFRNet):
    """MambaOFR with MGFE branch descriptors and optional recalibration."""

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
        super().__init__(num_feat=num_feat, use_checkpoint=use_checkpoint, **kwargs)
        self.use_mgfe = use_mgfe
        self.mgfe_num_tokens = mgfe_num_tokens
        self.mgfe_num_branches = mgfe_num_branches
        self.mgfe_token_fusion = mgfe_token_fusion
        self.mgfe = MGFE(
            in_channels=self.num_feat,
            num_tokens=mgfe_num_tokens,
            num_branches=mgfe_num_branches,
            token_fusion=mgfe_token_fusion,
            use_checkpoint=use_checkpoint,
        )
        self._branch_feats_cache = None

    def _run_mgfe(self, feat_prop: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
        recalibrated, branch_feats = self.mgfe(feat_prop)
        if self.use_mgfe:
            return recalibrated, branch_feats
        return feat_prop, branch_feats

    def get_branch_features(self) -> torch.Tensor | None:
        return self._branch_feats_cache

    def _backward_propagation(self, lrs, backward_flow, *, capture_intermediates=False):
        """Backward propagation shared by forward() and visualize_mgfe()."""
        n, t, _, h, w = lrs.size()
        cached_feats = []
        cached_branch_feats = []
        intermediates_bwd = [] if capture_intermediates else None

        feat_prop = lrs.new_zeros(n, self.num_feat, h, w)
        residual_indicator = lrs.new_zeros(n, 1, h, w)
        pre_mask = residual_indicator.new_ones(residual_indicator.shape)

        for i in range(t - 1, -1, -1):
            curr_lr = lrs[:, i, :, :, :]
            if i < t - 1:
                flow = backward_flow[:, i, :, :, :]
                feat_prop_o = feat_prop
                feat_prop = flow_warp(feat_prop, flow.permute(0, 2, 3, 1))

                pixel_prop = flow_warp(lrs[:, i + 1, :, :, :], flow.permute(0, 2, 3, 1))
                residual_indicator = torch.abs(pixel_prop[:, :1, :, :] - curr_lr[:, :1, :, :])
                pre_mask = flow_warp(pre_mask, flow.permute(0, 2, 3, 1))

                feat_prop, pre_mask = self.Backward_Aggregation(
                    feat_prop, curr_lr, residual_indicator,
                    feat_prop_o, flow, pre_mask=pre_mask, head=False,
                )
            else:
                feat_prop, pre_mask = self.Backward_Aggregation(
                    feat_prop, curr_lr, residual_indicator,
                    pre_mask=pre_mask, head=True,
                )

            feat_prop = self.backward_resblocks(feat_prop)

            if capture_intermediates:
                feat_before = feat_prop
                inter = self.mgfe.forward_with_intermediates(feat_prop)
                feat_prop = inter['output'] if self.use_mgfe else feat_prop
                branch_feats = inter['branch_descriptors']
                inter['recalibration_delta'] = (feat_prop - feat_before).abs().mean(dim=1, keepdim=True)
                intermediates_bwd.append(inter)
            else:
                feat_prop, branch_feats = self._run_mgfe(feat_prop)

            cached_feats.append(feat_prop)
            cached_branch_feats.append(branch_feats)

        cached_feats.reverse()
        cached_branch_feats.reverse()
        if intermediates_bwd is not None:
            intermediates_bwd.reverse()

        return cached_feats, cached_branch_feats, intermediates_bwd

    def _forward_propagation_and_reconstruct(
        self, lrs, forward_flow, cached_feats, cached_branch_feats,
        *, capture_intermediates=False,
    ):
        """Forward propagation + reconstruction shared by forward() and visualize_mgfe()."""
        n, t, _, h, w = lrs.size()
        outputs = []
        output_branch_feats = []
        intermediates_fwd = [] if capture_intermediates else None

        feat_prop = lrs.new_zeros(n, self.num_feat, h, w)
        residual_indicator = lrs.new_zeros(n, 1, h, w)
        pre_mask = residual_indicator.new_ones(residual_indicator.shape)

        for i in range(t):
            curr_lr = lrs[:, i, :, :, :]
            if i > 0:
                flow = forward_flow[:, i - 1, :, :, :]
                feat_prop_o = feat_prop
                feat_prop = flow_warp(feat_prop, flow.permute(0, 2, 3, 1))

                pixel_prop = flow_warp(lrs[:, i - 1, :, :, :], flow.permute(0, 2, 3, 1))
                residual_indicator = torch.abs(pixel_prop[:, :1, :, :] - curr_lr[:, :1, :, :])
                pre_mask = flow_warp(pre_mask, flow.permute(0, 2, 3, 1))

                feat_prop, pre_mask = self.Forward_Aggregation(
                    feat_prop, curr_lr, residual_indicator,
                    feat_prop_o, flow, pre_mask=pre_mask, head=False,
                )
            else:
                feat_prop, pre_mask = self.Forward_Aggregation(
                    feat_prop, curr_lr, residual_indicator,
                    pre_mask=pre_mask, head=True,
                )

            feat_prop = self.forward_resblocks(feat_prop)

            if capture_intermediates:
                feat_before = feat_prop
                inter = self.mgfe.forward_with_intermediates(feat_prop)
                feat_prop = inter['output'] if self.use_mgfe else feat_prop
                forward_branch_feats = inter['branch_descriptors']
                inter['recalibration_delta'] = (feat_prop - feat_before).abs().mean(dim=1, keepdim=True)
                intermediates_fwd.append(inter)
            else:
                feat_prop, forward_branch_feats = self._run_mgfe(feat_prop)

            backward_feat = cached_feats[i]
            forward_feat = feat_prop

            if self.paf_module is not None:
                backward_feat = self.paf_module(backward_feat, forward_feat)
                forward_feat = self.paf_module(forward_feat, backward_feat)

            cat_feat = torch.cat([backward_feat, forward_feat], dim=1)
            sr_rlt = self.lrelu(self.concate(cat_feat))
            sr_rlt = self.lrelu(self.up1(sr_rlt))
            sr_rlt = self.lrelu(self.up2(sr_rlt))
            sr_rlt = self.lrelu(self.conv_hr(sr_rlt))
            sr_rlt = self.conv_last(sr_rlt)

            base = self.img_up(curr_lr)
            outputs.append(torch.tanh(sr_rlt + base))
            output_branch_feats.append(0.5 * (cached_branch_feats[i] + forward_branch_feats))

        if output_branch_feats:
            self._branch_feats_cache = torch.stack(output_branch_feats, dim=1)

        return outputs, intermediates_fwd

    def forward(self, lrs: torch.Tensor) -> torch.Tensor:
        n, t, _, h, w = lrs.size()
        self._branch_feats_cache = None
        assert h >= 64 and w >= 64, f'Input resolution must be at least 64x64, got {h}x{w}'

        forward_flow, backward_flow = self.comp_flow(lrs)
        cached_feats, cached_branch_feats, _ = self._backward_propagation(
            lrs, backward_flow, capture_intermediates=False,
        )
        outputs, _ = self._forward_propagation_and_reconstruct(
            lrs, forward_flow, cached_feats, cached_branch_feats,
            capture_intermediates=False,
        )
        return torch.stack(outputs, dim=1)

    def visualize_mgfe(self, lrs: torch.Tensor) -> dict[str, torch.Tensor]:
        """Visualize MGFE innovation: recalibration maps, branch diversity, per frame.

        Runs full forward with intermediate capture at every MGFE call site.

        Returns dict with (B, T, ...) tensors:
            mgfe_scale_map_bwd / _fwd: (B, T, 1, H, W) — recalibration scale spatial map
            mgfe_shift_map_bwd / _fwd: (B, T, 1, H, W) — recalibration shift spatial map
            recalibration_delta_bwd / _fwd: (B, T, 1, H, W) — L1 feature delta
            branch_sim_bwd / _fwd: (B, T, G, G) — per-frame branch cosine similarity
            branch_feats_cache: (B, T, G, C) — fwd+bwd averaged branch descriptors
        """
        n, t, _, h, w = lrs.size()
        assert h >= 64 and w >= 64, f'Input resolution must be at least 64x64, got {h}x{w}'

        forward_flow, backward_flow = self.comp_flow(lrs)

        cached_feats, cached_branch_feats, intermediates_bwd = self._backward_propagation(
            lrs, backward_flow, capture_intermediates=True,
        )
        _, intermediates_fwd = self._forward_propagation_and_reconstruct(
            lrs, forward_flow, cached_feats, cached_branch_feats,
            capture_intermediates=True,
        )

        def _stack_key(inter_list, key):
            return torch.stack([d[key] for d in inter_list], dim=1)

        result = {
            'mgfe_scale_map_bwd': _stack_key(intermediates_bwd, 'scale_map'),
            'mgfe_scale_map_fwd': _stack_key(intermediates_fwd, 'scale_map'),
            'mgfe_shift_map_bwd': _stack_key(intermediates_bwd, 'shift_map'),
            'mgfe_shift_map_fwd': _stack_key(intermediates_fwd, 'shift_map'),
            'recalibration_delta_bwd': _stack_key(intermediates_bwd, 'recalibration_delta'),
            'recalibration_delta_fwd': _stack_key(intermediates_fwd, 'recalibration_delta'),
            'branch_sim_bwd': _stack_key(intermediates_bwd, 'branch_similarity'),
            'branch_sim_fwd': _stack_key(intermediates_fwd, 'branch_similarity'),
        }

        if self._branch_feats_cache is not None:
            result['branch_feats_cache'] = self._branch_feats_cache

        return result
