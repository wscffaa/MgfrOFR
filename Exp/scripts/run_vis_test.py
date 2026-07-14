"""Run MGFE visualization test for 001-reidmamba (MGFROFR).

Usage (on L40 server):
    cd /mnt/data/Antigravity_OFR/framework
    CUDA_VISIBLE_DEVICES=1 python ../projects/001-reidmamba/Exp/scripts/run_vis_test.py \
        --variant a3 --dataset synthetic --num_clips 5

This script:
1. Loads the best checkpoint for the specified variant
2. Runs inference with _collect_visual_debug=True
3. Saves MGFE visualization PNGs to test output directory
"""

import argparse
import os
import sys

import numpy as np
import torch

OFR_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
sys.path.insert(0, os.path.join(OFR_ROOT, 'framework'))
os.chdir(OFR_ROOT)

from basicsr.data import build_dataloader, build_dataset
from basicsr.utils.registry import ARCH_REGISTRY, MODEL_REGISTRY

import basicofr.archs  # noqa: F401 — triggers auto-scan of projects/*/archs/
import basicofr.models  # noqa: F401 — triggers auto-scan of projects/*/models/
import basicofr.losses  # noqa: F401 — triggers auto-scan of projects/*/losses/


VARIANT_CONFIG = {
    'a0': {
        'name': 'mgfrofr_a0_baseline',
        'ckpt': 'projects/015-reidmamba/Exp/experiments/mgfrofr_a0_baseline/models/net_g_145000.pth',
        'use_mgfe': False,
    },
    'a1': {
        'name': 'mgfrofr_a1_mgfe',
        'ckpt': 'projects/015-reidmamba/Exp/experiments/mgfrofr_a1_mgfe/models/net_g_145000.pth',
        'use_mgfe': True,
    },
    'a2': {
        'name': 'mgfrofr_a2_ratr',
        'ckpt': 'projects/015-reidmamba/Exp/experiments/mgfrofr_a2_ratr/models/net_g_145000.pth',
        'use_mgfe': False,
    },
    'a3': {
        'name': 'mgfrofr_a3_full',
        'ckpt': 'projects/015-reidmamba/Exp/experiments/mgfrofr_a3_full/models/net_g_145000.pth',
        'use_mgfe': True,
    },
}

DATASET_CONFIG = {
    'synthetic': {
        'name': 'REDS_synthetic',
        'dataroot_gt': 'datasets/OldFilmRestoration/val/REDS/GT/val_sharp',
        'dataroot_lq': 'datasets/OldFilmRestoration/val/REDS/LQ/val_sharp_degraded',
    },
    'realworld': {
        'name': 'RealFilm_SRWOV',
        'dataroot_gt': None,
        'dataroot_lq': 'datasets/OldFilmRestoration/val/SRWOV/LQ',
    },
}


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--variant', choices=['a0', 'a1', 'a2', 'a3'], default='a3')
    parser.add_argument('--dataset', choices=['synthetic', 'realworld'], default='synthetic')
    parser.add_argument('--num_clips', type=int, default=5,
                        help='Number of clips to process (0 = all)')
    parser.add_argument('--output_dir', default=None,
                        help='Custom output dir (default: auto)')
    return parser.parse_args()


def build_opt(args):
    variant = VARIANT_CONFIG[args.variant]
    ds = DATASET_CONFIG[args.dataset]

    opt = {
        'name': f'vis_{variant["name"]}_{ds["name"]}',
        'model_type': 'MGFROFRModel',
        'scale': 1,
        'num_gpu': 1,
        'dist': False,
        'is_train': False,
        'datasets': {
            'test': {
                'name': ds['name'],
                'type': 'Film_dataset_1',
                'dataroot_lq': ds['dataroot_lq'],
                'num_frame': -1,
                'cache_data': True,
                'normalizing': True,
                'scale': 1,
                'phase': 'test',
                'io_backend': {'type': 'disk'},
            }
        },
        'network_g': {
            'type': 'MgfrOFR',
            'num_feat': 16,
            'num_block': 6,
            'flow_type': 'raft',
            'use_checkpoint': False,
            'mamba_embed_dim': 64,
            'mamba_depths': [2, 2, 2],
            'mamba_d_state': 16,
            'mamba_mlp_ratio': 1.2,
            'mamba_drop_path': 0.0,
            'use_mgfe': variant['use_mgfe'],
            'mgfe_num_tokens': 12,
            'mgfe_num_branches': 3,
            'mgfe_token_fusion': 'max',
        },
        'path': {
            'pretrain_network_g': variant['ckpt'],
            'results_root': args.output_dir or f'projects/001-reidmamba/Exp/vis_output/{variant["name"]}_{ds["name"]}',
        },
        'val': {
            'save_img': True,
        },
    }

    if ds['dataroot_gt'] is not None:
        opt['datasets']['test']['dataroot_gt'] = ds['dataroot_gt']

    return opt


def _save_spatial_maps(output_dir, frame_name, mgfe_data, local_idx):
    """Save MGFE spatial maps as grayscale PNGs."""
    from basicsr.utils import imwrite

    mgfe_dir = os.path.join(output_dir, 'mgfe')
    os.makedirs(mgfe_dir, exist_ok=True)
    img_stem = os.path.splitext(frame_name)[0]

    import torch as _torch
    spatial_keys = [k for k, v in mgfe_data.items()
                    if isinstance(v, _torch.Tensor) and v.dim() >= 3
                    and k not in ('branch_sim_bwd', 'branch_sim_fwd')]
    for key in spatial_keys:
        tensor = mgfe_data[key]
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
        img = (np.clip(arr, 0.0, 1.0) * 255.0).round().astype(np.uint8)
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


def main():
    args = parse_args()
    opt = build_opt(args)
    variant = VARIANT_CONFIG[args.variant]

    log_dir = os.path.join(OFR_ROOT, os.path.dirname(opt['path']['results_root']))
    os.makedirs(log_dir, exist_ok=True)

    ckpt_path = os.path.join(OFR_ROOT, variant['ckpt'])
    if not os.path.exists(ckpt_path):
        print(f"[ERROR] Checkpoint not found: {ckpt_path}")
        sys.exit(1)

    print(f"=== MGFROFR Visualization Test ===")
    print(f"  Variant:    {args.variant} ({variant['name']})")
    print(f"  Dataset:    {args.dataset}")
    print(f"  Checkpoint: {variant['ckpt']}")
    print(f"  use_mgfe:   {variant['use_mgfe']}")
    print(f"  Output:     {opt['path']['results_root']}")
    print()

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    net_g = ARCH_REGISTRY.get(opt['network_g']['type'])(**{
        k: v for k, v in opt['network_g'].items() if k != 'type'
    })
    state_dict = torch.load(ckpt_path, map_location='cpu', weights_only=True)
    if 'params' in state_dict:
        state_dict = state_dict['params']
    elif 'params_ema' in state_dict:
        state_dict = state_dict['params_ema']
    strict = variant['use_mgfe']
    net_g.load_state_dict(state_dict, strict=strict)
    net_g = net_g.to(device)
    net_g.eval()

    test_ds = build_dataset(opt['datasets']['test'])
    test_loader = build_dataloader(
        test_ds, opt['datasets']['test'],
        num_gpu=1, dist=False, sampler=None, seed=2021,
    )

    output_root = os.path.join(OFR_ROOT, opt['path']['results_root'])
    os.makedirs(output_root, exist_ok=True)

    print(f"  Total clips: {len(test_ds)}")
    num_clips = args.num_clips if args.num_clips > 0 else len(test_ds)
    print(f"  Processing:  {num_clips} clips")
    print()

    for clip_idx, data in enumerate(test_loader):
        if clip_idx >= num_clips:
            break

        folder = data.get('folder', [f'clip_{clip_idx:04d}'])[0]
        lq = data['lq'].to(device)

        print(f"  [{clip_idx+1}/{num_clips}] {folder} — shape {tuple(lq.shape)}")

        with torch.no_grad():
            output = net_g(lq)

            mgfe_data = None
            if hasattr(net_g, 'visualize_mgfe') and variant['use_mgfe']:
                mgfe_data = net_g.visualize_mgfe(lq)
                mgfe_data = {
                    k: v.detach().cpu()[0] if isinstance(v, torch.Tensor) else v
                    for k, v in mgfe_data.items()
                }

            feature_data = None
            if hasattr(net_g, 'visualiza_feature'):
                try:
                    feat_out = net_g.visualiza_feature(lq)
                    if isinstance(feat_out, (list, tuple)) and len(feat_out) == 4:
                        b_feat, b_state, f_feat, f_state = feat_out
                        feature_data = {}
                        if b_feat is not None:
                            feature_data['baseline_feat_bwd'] = b_feat.detach().cpu()[0]
                        if f_feat is not None:
                            feature_data['baseline_feat_fwd'] = f_feat.detach().cpu()[0]
                except Exception:
                    pass

        clip_dir = os.path.join(output_root, folder)

        if mgfe_data is not None:
            t_frames = lq.size(1)
            for frame_idx in range(t_frames):
                frame_name = f'{frame_idx:08d}.png'
                _save_spatial_maps(clip_dir, frame_name, mgfe_data, frame_idx)

        if feature_data is not None:
            t_frames = lq.size(1)
            for frame_idx in range(t_frames):
                frame_name = f'{frame_idx:08d}.png'
                _save_spatial_maps(clip_dir, frame_name, feature_data, frame_idx)

        print(f"    -> saved to {clip_dir}")

    print(f"\n=== Done. Output at {output_root} ===")


if __name__ == '__main__':
    main()
