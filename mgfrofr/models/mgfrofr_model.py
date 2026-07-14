import contextlib
import os
from collections import OrderedDict

import numpy as np
import torch

from basicsr.losses import build_loss
from basicsr.utils import imwrite
from basicsr.utils.profiler import profile, profiler
from basicsr.utils.registry import MODEL_REGISTRY


from basicofr.models.rtn_model import RTNGANModel
# RATRLoss is auto-registered by basicofr.losses scan (imported in train.py)


@MODEL_REGISTRY.register()
class MGFROFRModel(RTNGANModel):
    """RTN training loop with optional RATR regularization."""

    def init_training_settings(self):
        super().init_training_settings()

        train_opt = self.opt['train']
        self.use_ratr = train_opt.get('use_ratr', False)

        if self.use_ratr:
            if not train_opt.get('ratr_opt'):
                raise ValueError('train.ratr_opt must be provided when train.use_ratr is true.')
            self.cri_ratr = build_loss(train_opt['ratr_opt']).to(self.device)
            self.ratr_loss_weight = train_opt.get('ratr_loss_weight', 1.0)
        else:
            self.cri_ratr = None
            self.ratr_loss_weight = 0.0

    def _get_net_g_module(self):
        return self.net_g.module if hasattr(self.net_g, 'module') else self.net_g

    def optimize_parameters(self, current_iter):
        self._manage_flow_freeze(current_iter)

        for p in self.net_d.parameters():
            p.requires_grad = True
        self.optimizer_d.zero_grad()

        amp_autocast = contextlib.nullcontext
        if self.use_amp:
            from functools import partial
            from torch.amp import autocast
            amp_autocast = partial(autocast, 'cuda')

        with amp_autocast():
            with profile('G forward'):
                self.output = self.net_g(self.lq)

        loss_dict = OrderedDict()

        gt_for_d = self.gt
        output_for_d = self.output
        if not getattr(self, '_discriminator_expects_3d', False):
            if self.gt.dim() == 5:
                b, t, c, h, w = self.gt.size()
                gt_for_d = self.gt.reshape(b * t, c, h, w)
            if self.output.dim() == 5:
                b, t, c, h, w = self.output.size()
                output_for_d = self.output.reshape(b * t, c, h, w)

        with amp_autocast():
            with profile('D forward (real)'):
                real_pred = self.net_d(gt_for_d)
            loss_d_real = self.cri_gan(real_pred, True, is_disc=True)
            with profile('D forward (fake)'):
                fake_pred = self.net_d(output_for_d.detach())
            loss_d_fake = self.cri_gan(fake_pred, False, is_disc=True)
            l_d_total = 0.5 * (loss_d_real + loss_d_fake) * self.d_gan_weight

        loss_dict['l_d_real'] = loss_d_real
        loss_dict['out_d_real'] = torch.mean(real_pred.detach())
        loss_dict['l_d_fake'] = loss_d_fake
        loss_dict['out_d_fake'] = torch.mean(fake_pred.detach())
        loss_dict['l_d'] = l_d_total

        if self.use_amp:
            with profile('D backward'):
                self.scaler_d.scale(l_d_total).backward()
            with profile('D step'):
                self.scaler_d.step(self.optimizer_d)
                self.scaler_d.update()
        else:
            with profile('D backward'):
                l_d_total.backward()
            with profile('D step'):
                self.optimizer_d.step()

        for p in self.net_d.parameters():
            p.requires_grad = False

        if self.accumulation_counter == 0:
            self.optimizer_g.zero_grad()

        with amp_autocast():
            l_g_total = 0.0

            if self.cri_pix:
                with profile('Pixel loss (cri_pix)'):
                    l_g_pix = self.cri_pix(self.output, self.gt)
                l_g_total += l_g_pix
                loss_dict['l_g_pix'] = l_g_pix

            if self.cri_perceptual:
                with profile('Perceptual loss + VGG'):
                    if self.output.dim() == 5:
                        b, t, c, h, w = self.output.size()
                        pred = self.output.reshape(b * t, c, h, w)
                        gt = self.gt.reshape(b * t, c, h, w)
                        percep_result = self.cri_perceptual(pred, gt)
                    else:
                        percep_result = self.cri_perceptual(self.output, self.gt)

                l_g_percep = percep_result[0] if isinstance(percep_result, tuple) else percep_result
                l_g_total += l_g_percep
                loss_dict['l_g_percep'] = l_g_percep

            with profile('GAN loss (G cri_gan)'):
                fake_g_pred = self.net_d(output_for_d)
                l_g_gan = self.cri_gan(fake_g_pred, True, is_disc=False) * self.g_gan_weight
            l_g_total += l_g_gan
            loss_dict['l_g_gan'] = l_g_gan

            if self.cri_ratr is not None:
                branch_feats = None
                net_g = self._get_net_g_module()
                if hasattr(net_g, 'get_branch_features'):
                    branch_feats = net_g.get_branch_features()
                if branch_feats is None:
                    raise RuntimeError('RATR is enabled but generator did not provide branch features.')
                with profile('RATR loss'):
                    l_ratr = self.cri_ratr(branch_feats)
                l_g_total += l_ratr * self.ratr_loss_weight
                loss_dict['l_ratr'] = l_ratr

            if self.accumulation_steps > 1:
                l_g_total = l_g_total / float(self.accumulation_steps)

        if self.use_amp:
            with profile('G backward'):
                self.scaler_g.scale(l_g_total).backward()
        else:
            with profile('G backward'):
                l_g_total.backward()

        if (self.accumulation_counter + 1) % self.accumulation_steps == 0:
            if self.use_amp:
                with profile('G step'):
                    self.scaler_g.step(self.optimizer_g)
                    self.scaler_g.update()
            else:
                with profile('G step'):
                    self.optimizer_g.step()
            self.optimizer_g.zero_grad()

        self.accumulation_counter = (self.accumulation_counter + 1) % self.accumulation_steps

        self.log_dict = self.reduce_loss_dict(loss_dict)
        if self.ema_decay > 0:
            self.model_ema(decay=self.ema_decay)

        self._save_training_visualization(current_iter)
        profiler.report_and_reset(current_iter)
        self._optimizer_stepped = True

    def test(self):
        use_ema = hasattr(self, 'ema_decay') and self.ema_decay > 0
        net = self.net_g_ema if use_ema else self.net_g

        prev_training_state = net.training
        net.eval()

        collect_debug = getattr(self, '_collect_visual_debug', False)
        self._last_visual_masks = None
        self._last_visual_features = None
        self._last_mgfe_data = None

        with torch.no_grad():
            self.output = net(self.lq)

            if collect_debug:
                if hasattr(net, 'visualiza_mask'):
                    try:
                        backward_mask, forward_mask = net.visualiza_mask(self.lq)
                        self._last_visual_masks = {
                            'backward': backward_mask.detach().cpu()[0],
                            'forward': forward_mask.detach().cpu()[0],
                        }
                    except Exception:
                        pass

                if hasattr(net, 'visualiza_feature'):
                    try:
                        feature_outputs = net.visualiza_feature(self.lq)
                    except Exception:
                        feature_outputs = None
                    if feature_outputs is not None:
                        features = {}
                        if isinstance(feature_outputs, (list, tuple)) and len(feature_outputs) == 4:
                            b_feat, b_state, f_feat, f_state = feature_outputs
                            if b_feat is not None:
                                features['backward_mean_mask'] = b_feat.detach().cpu()[0]
                            if b_state is not None:
                                features['backward_state'] = b_state.detach().cpu()[0]
                            if f_feat is not None:
                                features['forward_mean_mask'] = f_feat.detach().cpu()[0]
                            if f_state is not None:
                                features['forward_state'] = f_state.detach().cpu()[0]
                        self._last_visual_features = features if features else None

                if hasattr(net, 'visualize_mgfe'):
                    try:
                        mgfe_data = net.visualize_mgfe(self.lq)
                        if mgfe_data:
                            self._last_mgfe_data = {
                                k: v.detach().cpu()[0] if isinstance(v, torch.Tensor) else v
                                for k, v in mgfe_data.items()
                            }
                    except Exception:
                        pass

        if not use_ema and prev_training_state:
            net.train()

    def _save_mgfe_images(self, output_dir, frame_name, mgfe_data, local_idx,
                          orig_h=None, orig_w=None):
        """Save MGFE visualization as pseudo-color PNG images."""
        if mgfe_data is None:
            return

        mgfe_dir = os.path.join(output_dir, 'mgfe')
        os.makedirs(mgfe_dir, exist_ok=True)
        img_stem = os.path.splitext(frame_name)[0]

        spatial_keys = [
            'mgfe_scale_map_bwd', 'mgfe_scale_map_fwd',
            'mgfe_shift_map_bwd', 'mgfe_shift_map_fwd',
            'recalibration_delta_bwd', 'recalibration_delta_fwd',
        ]

        for key in spatial_keys:
            tensor = mgfe_data.get(key)
            if tensor is None:
                continue
            if local_idx >= tensor.size(0):
                continue

            sub_dir = os.path.join(mgfe_dir, key)
            os.makedirs(sub_dir, exist_ok=True)

            arr = tensor[local_idx].squeeze().numpy()
            min_val, max_val = float(arr.min()), float(arr.max())
            if max_val > min_val:
                arr = (arr - min_val) / (max_val - min_val)
            else:
                arr = np.zeros_like(arr)
            arr = np.clip(arr, 0.0, 1.0)
            img = (arr * 255.0).round().astype(np.uint8)

            if orig_h is not None and orig_w is not None and img.ndim >= 2:
                if img.shape[0] >= orig_h and img.shape[1] >= orig_w:
                    img = img[:orig_h, :orig_w]

            imwrite(img, os.path.join(sub_dir, f'{img_stem}_{key}.png'))

        for sim_key in ['branch_sim_bwd', 'branch_sim_fwd']:
            tensor = mgfe_data.get(sim_key)
            if tensor is None or local_idx >= tensor.size(0):
                continue

            sub_dir = os.path.join(mgfe_dir, sim_key)
            os.makedirs(sub_dir, exist_ok=True)

            sim_matrix = tensor[local_idx].numpy()
            g = sim_matrix.shape[0]
            cell_size = 64
            canvas = np.zeros((g * cell_size, g * cell_size), dtype=np.uint8)
            for r in range(g):
                for c_idx in range(g):
                    val = np.clip((sim_matrix[r, c_idx] + 1.0) / 2.0, 0, 1)
                    canvas[r * cell_size:(r + 1) * cell_size,
                           c_idx * cell_size:(c_idx + 1) * cell_size] = int(val * 255)
            imwrite(canvas, os.path.join(sub_dir, f'{img_stem}_{sim_key}.png'))
