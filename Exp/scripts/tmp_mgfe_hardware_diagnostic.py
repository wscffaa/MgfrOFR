"""Temporary diagnostic: compare MGFE branch behavior under identical init/input across hardware.

This script is intentionally throw-away. It initializes a MgfrOFR network with the
A3 configuration, fixes torch/numpy/python RNG seeds, feeds a deterministic input,
and prints the MGFE branch similarity matrices and descriptor statistics obtained
via the existing net.visualize_mgfe() hook.

Run on each server (4090_1 with rtn27, L40 with rtn, A100 with rtn) and diff the
outputs to isolate hardware/driver-induced divergence in MGFE/RATR behavior.
"""

import argparse
import json
import os
import sys

OFR_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
FRAMEWORK_ROOT = os.path.join(OFR_ROOT, 'framework')


def parse_args():
    parser = argparse.ArgumentParser(description='MGFE hardware divergence diagnostic.')
    parser.add_argument('--config', default='projects/001-reidmamba/Exp/options/train/mgfrofr_a3.yml',
                        help='Training YAML whose network_g section defines the architecture.')
    parser.add_argument('--seed', type=int, default=2021, help='RNG seed for weight init and input.')
    parser.add_argument('--batch', type=int, default=1, help='Batch size N for input (N,T,C,H,W).')
    parser.add_argument('--frames', type=int, default=7, help='Number of frames T.')
    parser.add_argument('--height', type=int, default=256, help='Input height H.')
    parser.add_argument('--width', type=int, default=256, help='Input width W.')
    parser.add_argument('--load-ckpt', default=None, help='Optional checkpoint to load before measurement.')
    parser.add_argument('--output', default=None, help='Optional JSON path to write results.')
    parser.add_argument('--device', default='cuda', help='torch device.')
    return parser.parse_args()


def main():
    args = parse_args()

    # train.py changes cwd to framework/; mirror that so registry paths work.
    os.chdir(FRAMEWORK_ROOT)
    sys.path.insert(0, OFR_ROOT)
    sys.path.insert(0, FRAMEWORK_ROOT)

    import numpy as np
    import torch
    import yaml

    import basicofr.archs  # noqa: F401 — auto-scan project archs
    import basicofr.losses  # noqa: F401
    import basicofr.models  # noqa: F401
    from basicsr.utils.registry import ARCH_REGISTRY

    # Deterministic seeds.
    torch.manual_seed(args.seed)
    np.random.seed(args.seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(args.seed)

    # Load network_g from config.
    config_path = args.config if os.path.isabs(args.config) else os.path.join(OFR_ROOT, args.config)
    with open(config_path, 'r', encoding='utf-8') as fh:
        opt = yaml.safe_load(fh)
    network_g = opt['network_g']
    # Force use_checkpoint False for this deterministic forward diagnostic.
    network_g['use_checkpoint'] = False

    device = torch.device(args.device if torch.cuda.is_available() else 'cpu')
    net = ARCH_REGISTRY.get(network_g['type'])(**{k: v for k, v in network_g.items() if k != 'type'})
    net = net.to(device).eval()

    if args.load_ckpt:
        ckpt_path = args.load_ckpt if os.path.isabs(args.load_ckpt) else os.path.join(OFR_ROOT, args.load_ckpt)
        state = torch.load(ckpt_path, map_location='cpu', weights_only=True)
        if 'params' in state:
            state = state['params']
        elif 'params_ema' in state:
            state = state['params_ema']
        net.load_state_dict(state, strict=network_g.get('use_mgfe', True))

    # Deterministic input.
    torch.manual_seed(args.seed)
    np.random.seed(args.seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(args.seed)
    x = torch.randn(args.batch, args.frames, 3, args.height, args.width, device=device)

    with torch.no_grad():
        mgfe_data = net.visualize_mgfe(x)

    # Collect statistics.
    results = {
        'config': args.config,
        'seed': args.seed,
        'input_shape': list(x.shape),
        'device': str(device),
        'torch_version': torch.__version__,
        'cuda_version': torch.version.cuda,
        'network_g': {k: v for k, v in network_g.items() if k != 'type'},
        'load_ckpt': args.load_ckpt,
    }

    for key in ('branch_sim_bwd', 'branch_sim_fwd'):
        sim = mgfe_data.get(key)
        if sim is None:
            continue
        sim_np = sim.detach().cpu().numpy()
        g = sim_np.shape[-1]
        offdiag_mask = ~np.eye(g, dtype=bool)
        results[key] = {
            'shape': list(sim_np.shape),
            'mean': float(sim_np.mean()),
            'std': float(sim_np.std()),
            'offdiag_mean': float(sim_np[..., offdiag_mask].mean()),
            'offdiag_std': float(sim_np[..., offdiag_mask].std()),
            'matrix': sim_np.mean(axis=(0, 1)).tolist() if sim_np.ndim >= 3 else sim_np.tolist(),
        }

    branch_feats = mgfe_data.get('branch_feats_cache')
    if branch_feats is not None:
        bf_np = branch_feats.detach().cpu().numpy()
        results['branch_feats_cache'] = {
            'shape': list(bf_np.shape),
            'mean': float(bf_np.mean()),
            'std': float(bf_np.std()),
            'per_branch_mean': bf_np.mean(axis=(0, 1, -1)).tolist() if bf_np.ndim >= 4 else bf_np.mean(axis=-1).tolist(),
            'per_branch_std': bf_np.std(axis=(0, 1, -1)).tolist() if bf_np.ndim >= 4 else bf_np.std(axis=-1).tolist(),
        }

    print(json.dumps(results, indent=2))

    if args.output:
        out_path = args.output if os.path.isabs(args.output) else os.path.join(OFR_ROOT, args.output)
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, 'w', encoding='utf-8') as fh:
            json.dump(results, fh, indent=2)
        print(f'[diagnostic] wrote -> {out_path}', file=sys.stderr)


if __name__ == '__main__':
    main()
