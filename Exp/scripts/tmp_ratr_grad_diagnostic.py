"""Temporary diagnostic: does use_checkpoint break RATR gradient flow to MGFE branches?

Hypothesis: on 4090, training runs with use_checkpoint=true (small VRAM); the RATR
loss reads net_g.get_branch_features() (the cached branch descriptors). If gradient
checkpointing detaches / breaks the path from l_ratr back to MGFE branch_blocks, RATR
cannot push branch diversity, branches collapse, and l_ratr decays to ~0 — exactly
the observed failure. L40/A100 run use_checkpoint=false, so RATR works (l_ratr ~ -0.05).

This is a SINGLE-MACHINE test: same weights (fixed seed), same fixed input, only
use_checkpoint differs. We compare l_ratr value (should match, forward is numerically
identical) and the gradient norm reaching MGFE branch_blocks (the decisive signal).

Throw-away (tmp_ prefix, untracked).
"""

import argparse
import json
import os
import sys

OFR_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
FRAMEWORK_ROOT = os.path.join(OFR_ROOT, 'framework')


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument('--config', default='projects/001-reidmamba/Exp/options/train/mgfrofr_a3.yml')
    p.add_argument('--load-ckpt', default=None)
    p.add_argument('--seed', type=int, default=2021)
    p.add_argument('--frames', type=int, default=7)
    p.add_argument('--height', type=int, default=256)
    p.add_argument('--width', type=int, default=256)
    p.add_argument('--output', default=None)
    return p.parse_args()


def _abs(p):
    return p if os.path.isabs(p) else os.path.join(OFR_ROOT, p)


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
    from basicsr.utils.registry import ARCH_REGISTRY, LOSS_REGISTRY

    with open(_abs(args.config), 'r', encoding='utf-8') as fh:
        opt = yaml.safe_load(fh)
    base_ng = opt['network_g']
    ratr_opt = opt['train']['ratr_opt']
    tau = ratr_opt.get('tau', 0.1)
    iw = ratr_opt.get('intra_weight', 1.0)
    ew = ratr_opt.get('inter_weight', 1.0)
    lw = ratr_opt.get('loss_weight', 0.1)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    def seed_all():
        torch.manual_seed(args.seed)
        np.random.seed(args.seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(args.seed)

    def run(use_ckpt):
        ng = dict(base_ng)
        ng['use_checkpoint'] = use_ckpt
        seed_all()
        net = ARCH_REGISTRY.get(ng['type'])(**{k: v for k, v in ng.items() if k != 'type'}).to(device)
        if args.load_ckpt:
            st = torch.load(_abs(args.load_ckpt), map_location='cpu', weights_only=True)
            if isinstance(st, dict):
                st = st.get('params', st.get('params_ema', st))
            net.load_state_dict(st, strict=ng.get('use_mgfe', True))
        net.train()
        net.zero_grad(set_to_none=True)

        seed_all()
        x = torch.randn(1, args.frames, 3, args.height, args.width, device=device)

        out = net(x)
        bf = net.get_branch_features()
        if bf is None:
            raise RuntimeError('get_branch_features() returned None')
        bf.retain_grad()

        cri = LOSS_REGISTRY.get('RATRLoss')(
            tau=tau, intra_weight=iw, inter_weight=ew, loss_weight=lw).to(device)
        l_ratr = cri(bf)
        l_ratr.backward()

        mgfe = net.mgfe
        def grad_norm(params):
            sq = 0.0
            n_with = 0
            n_tot = 0
            for p in params:
                n_tot += 1
                if p.grad is not None:
                    sq += float(p.grad.detach().pow(2).sum().item())
                    n_with += 1
            return sq ** 0.5, n_with, n_tot

        bb_gn, bb_with, bb_tot = grad_norm(mgfe.branch_blocks.parameters())
        rc_gn, rc_with, rc_tot = grad_norm(mgfe.recalibrate.parameters())
        tok_gn, tok_with, tok_tot = grad_norm([mgfe.restoration_tokens])

        return {
            'use_checkpoint': use_ckpt,
            'l_ratr': float(l_ratr.item()),
            'bf_requires_grad': bool(bf.requires_grad),
            'bf_grad_norm': float(bf.grad.norm().item()) if bf.grad is not None else None,
            'branch_blocks_grad_norm': bb_gn,
            'branch_blocks_params_with_grad': f'{bb_with}/{bb_tot}',
            'recalibrate_grad_norm': rc_gn,
            'recalibrate_params_with_grad': f'{rc_with}/{rc_tot}',
            'restoration_tokens_grad_norm': tok_gn,
        }

    result = {
        'config': args.config,
        'load_ckpt': args.load_ckpt,
        'torch': torch.__version__,
        'cuda': torch.version.cuda,
        'device': torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'cpu',
        'runs': [run(False), run(True)],
    }
    print(json.dumps(result, indent=2))
    if args.output:
        op = _abs(args.output)
        os.makedirs(os.path.dirname(op), exist_ok=True)
        with open(op, 'w', encoding='utf-8') as fh:
            json.dump(result, fh, indent=2)
        print(f'[ratr-grad] wrote -> {op}', file=sys.stderr)


if __name__ == '__main__':
    main()
