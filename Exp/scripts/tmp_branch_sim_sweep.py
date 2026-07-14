"""Temporary diagnostic: sweep MGFE branch_sim off-diagonal across training checkpoints.

Extends tmp_mgfe_hardware_diagnostic.py from a single checkpoint to a full sweep.
One import, one fixed deterministic input reused for ALL checkpoints, so the only
变量 between points is the trained weights. Answers RATR-collapse question 4.1:
does the inter-branch cosine similarity rise toward 1.0 as training proceeds?

Debug-First: fails loudly on missing ckpt / missing visualize_mgfe / missing
branch_sim. Never fabricates values. Throw-away (tmp_ prefix, untracked).
"""

import argparse
import glob
import json
import os
import re
import sys

OFR_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
FRAMEWORK_ROOT = os.path.join(OFR_ROOT, 'framework')


def parse_args():
    p = argparse.ArgumentParser(description='Sweep checkpoints; record MGFE branch_sim off-diagonal evolution.')
    p.add_argument('--config', required=True, help='Training YAML; network_g defines architecture.')
    p.add_argument('--ckpt-dir', required=True, help='Dir with net_g_<iter>.pth (rel to OFR root or abs).')
    p.add_argument('--iters', default=None, help='Comma-separated iters; default auto-discover all.')
    p.add_argument('--seed', type=int, default=2021)
    p.add_argument('--frames', type=int, default=7)
    p.add_argument('--height', type=int, default=256)
    p.add_argument('--width', type=int, default=256)
    p.add_argument('--include-init', action='store_true', help='Also measure random-init (iter 0) baseline.')
    p.add_argument('--output', required=True)
    return p.parse_args()


def _abs(path):
    return path if os.path.isabs(path) else os.path.join(OFR_ROOT, path)


def main():
    args = parse_args()
    os.chdir(FRAMEWORK_ROOT)
    sys.path.insert(0, OFR_ROOT)
    sys.path.insert(0, FRAMEWORK_ROOT)

    import numpy as np
    import torch
    import yaml

    import basicofr.archs  # noqa: F401
    import basicofr.losses  # noqa: F401
    import basicofr.models  # noqa: F401
    from basicsr.utils.registry import ARCH_REGISTRY

    with open(_abs(args.config), 'r', encoding='utf-8') as fh:
        opt = yaml.safe_load(fh)
    network_g = opt['network_g']
    network_g['use_checkpoint'] = False
    use_mgfe = network_g.get('use_mgfe', True)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    ckpt_dir = _abs(args.ckpt_dir)
    if not os.path.isdir(ckpt_dir):
        raise FileNotFoundError(f'ckpt-dir does not exist: {ckpt_dir}')
    found = {}
    for path in glob.glob(os.path.join(ckpt_dir, 'net_g_*.pth')):
        m = re.search(r'net_g_(\d+)\.pth$', os.path.basename(path))
        if m:
            found[int(m.group(1))] = path
    want = [int(x) for x in args.iters.split(',') if x.strip()] if args.iters else sorted(found)
    missing = [i for i in want if i not in found]
    if missing:
        raise FileNotFoundError(f'requested iters not present in {ckpt_dir}: {missing}')

    def seed_all():
        torch.manual_seed(args.seed)
        np.random.seed(args.seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(args.seed)

    def build_net():
        seed_all()
        net = ARCH_REGISTRY.get(network_g['type'])(
            **{k: v for k, v in network_g.items() if k != 'type'})
        return net.to(device).eval()

    def offdiag_mean(sim):
        s = sim.detach().cpu().numpy()
        g = s.shape[-1]
        if g < 2:
            raise ValueError(f'branch-sim matrix has G={g}; need >=2 branches.')
        mask = ~np.eye(g, dtype=bool)
        return float(s[..., mask].mean())

    def measure(net, x):
        with torch.no_grad():
            if not hasattr(net, 'visualize_mgfe'):
                raise AttributeError('net_g has no visualize_mgfe hook.')
            mgfe = net.visualize_mgfe(x)
        out = {}
        for k in ('branch_sim_bwd', 'branch_sim_fwd'):
            sim = mgfe.get(k)
            if sim is not None:
                out[k] = offdiag_mean(sim)
        if out.get('branch_sim_bwd') is None and out.get('branch_sim_fwd') is None:
            raise KeyError('visualize_mgfe returned no branch_sim_bwd/branch_sim_fwd.')
        bf = mgfe.get('branch_feats_cache')
        if bf is not None:
            b = bf.detach().cpu().numpy()
            out['feat_per_branch_std'] = (
                b.std(axis=(0, 1, -1)).tolist() if b.ndim >= 4 else b.std(axis=-1).tolist())
        return out

    # Fixed input generated ONCE, reused for every checkpoint.
    seed_all()
    x = torch.randn(1, args.frames, 3, args.height, args.width, device=device)

    points = []

    if args.include_init:
        net = build_net()  # random-init MGFE, no checkpoint loaded
        m = measure(net, x)
        m['iter'] = 0
        points.append(m)
        print(f"iter={0:>7d}  bwd={m.get('branch_sim_bwd'):.4f}  fwd={m.get('branch_sim_fwd'):.4f}  "
              f"feat_std={[round(v,3) for v in m.get('feat_per_branch_std', [])]}")

    net = build_net()
    for it in want:
        state = torch.load(found[it], map_location='cpu', weights_only=True)
        if 'params' in state:
            state = state['params']
        elif 'params_ema' in state:
            state = state['params_ema']
        net.load_state_dict(state, strict=use_mgfe)
        net.eval()
        m = measure(net, x)
        m['iter'] = it
        points.append(m)
        print(f"iter={it:>7d}  bwd={m.get('branch_sim_bwd'):.4f}  fwd={m.get('branch_sim_fwd'):.4f}  "
              f"feat_std={[round(v,3) for v in m.get('feat_per_branch_std', [])]}")

    result = {
        'config': args.config,
        'ckpt_dir': args.ckpt_dir,
        'seed': args.seed,
        'input_shape': [1, args.frames, 3, args.height, args.width],
        'use_mgfe': use_mgfe,
        'num_branches': network_g.get('mgfe_num_branches'),
        'torch_version': torch.__version__,
        'cuda_version': torch.version.cuda,
        'metric': 'mean_offdiagonal_cosine_similarity(branch_sim_bwd/fwd), fixed deterministic input',
        'points': points,
    }
    out = _abs(args.output)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w', encoding='utf-8') as fh:
        json.dump(result, fh, indent=2)
    print(f'[sweep] wrote {len(points)} points -> {out}', file=sys.stderr)


if __name__ == '__main__':
    main()
