"""Diagnose RATR signal health on real MGFE branch descriptors (001-reidmamba).

Loads a variant's real checkpoint, runs real validation clips through the model,
extracts ``branch_feats_cache`` (B, T, G, C), and reports:

  - descriptor geometry: descr_abs_mean, cross_frame_std, const:fluct ratio,
    rel_frame_var, cross_branch_cos;
  - ``l_ratr`` WITH the time-centering fix (current ``RATRLoss``) vs WITHOUT it
    (pre-fix baseline) on the *same* real descriptors.

Purpose: confirm whether the time-centering fix restores a non-trivial RATR
signal on the real b1/t1 descriptors that collapsed to ~0 during training
(training logs: b1=4e-6, t1=1e-6 vs healthy a3=-0.057).

Usage (on a GPU server, run from the framework dir):
    cd <code_path>/framework
    CUDA_VISIBLE_DEVICES=1 python ../projects/001-reidmamba/Exp/scripts/diagnose_ratr_signal.py \
        --variant b1 --num_clips 3 --num_frames 7

Self-test (no checkpoint / GPU needed, synthetic constant-dominated descriptors):
    python projects/001-reidmamba/Exp/scripts/diagnose_ratr_signal.py --synthetic
"""
from __future__ import annotations

import argparse
import glob
import os
import re
import sys
from itertools import combinations

import torch
import torch.nn.functional as F
import yaml

OFR_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
sys.path.insert(0, os.path.join(OFR_ROOT, 'framework'))

import basicofr.archs  # noqa: E402,F401  triggers arch auto-scan
import basicofr.models  # noqa: E402,F401  triggers model auto-scan
import basicofr.losses  # noqa: E402,F401  triggers loss auto-scan + RATRLoss registration
from basicsr.data import build_dataloader, build_dataset  # noqa: E402
from basicsr.losses import build_loss  # noqa: E402
from basicsr.utils.registry import ARCH_REGISTRY  # noqa: E402

TRAIN_OPT_DIR = os.path.join(OFR_ROOT, 'projects/001-reidmamba/Exp/options/train')
EXP_DIR = os.path.join(OFR_ROOT, 'projects/001-reidmamba/Exp/experiments')


def load_variant_opt(variant: str) -> dict:
    path = os.path.join(TRAIN_OPT_DIR, f'mgfrofr_{variant}.yml')
    if not os.path.exists(path):
        raise FileNotFoundError(f'variant config not found: {path}')
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def find_checkpoint(exp_name: str, override: str | None) -> str:
    if override:
        path = override if os.path.isabs(override) else os.path.join(OFR_ROOT, override)
        if not os.path.exists(path):
            raise FileNotFoundError(f'checkpoint override not found: {path}')
        return path
    models_dir = os.path.join(EXP_DIR, exp_name, 'models')
    best = os.path.join(models_dir, 'net_g_best.pth')
    if os.path.exists(best):
        return best
    cands = glob.glob(os.path.join(models_dir, 'net_g_*.pth'))

    def iter_of(p: str) -> int:
        m = re.search(r'net_g_(\d+)\.pth$', p)
        return int(m.group(1)) if m else -1

    cands = [c for c in cands if iter_of(c) >= 0]
    if not cands:
        raise FileNotFoundError(f'no net_g checkpoint under {models_dir}')
    return max(cands, key=iter_of)


_ARCH_MODULE = {
    'MgfrOFR': 'archs.mgfrofr_arch',
    'MgfrOFRAggMax': 'archs.mgfrofr_aggmax_arch',
    'MgfrOFRInsertPrepend': 'archs.mgfrofr_insert_arch',
}


def _ensure_arch_registered(arch_type: str) -> None:
    """basicofr arch auto-scan uses a non-deterministic glob order; the mgfrofr
    module (MgfrOFR subclasses MambaOFRNet) is occasionally skipped when a sibling
    re-registration aborts its load, leaving MgfrOFR unregistered. If missing,
    import the module explicitly. Guarded so we never double-register on success.
    """
    if arch_type in ARCH_REGISTRY or f'{arch_type}_basicsr' in ARCH_REGISTRY:
        return
    module = _ARCH_MODULE.get(arch_type)
    if module is None:
        return
    proj_root = os.path.join(OFR_ROOT, 'projects/001-reidmamba')
    if proj_root not in sys.path:
        sys.path.insert(0, proj_root)
    import importlib
    importlib.import_module(module)


def build_net(network_opt: dict, ckpt_path: str, device: torch.device):
    _ensure_arch_registered(network_opt['type'])
    net = ARCH_REGISTRY.get(network_opt['type'])(
        **{k: v for k, v in network_opt.items() if k != 'type'}
    )
    state = torch.load(ckpt_path, map_location='cpu', weights_only=True)
    if isinstance(state, dict) and 'params' in state:
        state = state['params']
    elif isinstance(state, dict) and 'params_ema' in state:
        state = state['params_ema']
    net.load_state_dict(state, strict=True)
    return net.eval().to(device)


def descriptor_geometry(bfc: torch.Tensor) -> dict:
    """bfc: (B, T, G, C) float. Geometry metrics describing the b1/t1 collapse."""
    bfc = bfc.float()
    descr_abs_mean = bfc.abs().mean().item()
    cross_frame_std = bfc.std(dim=1, unbiased=False).mean().item()  # std over T
    ratio = descr_abs_mean / max(cross_frame_std, 1e-12)
    frame_var = bfc.var(dim=1, unbiased=False)             # (B,G,C) variance over T
    total_msq = bfc.pow(2).mean(dim=1).clamp_min(1e-12)    # (B,G,C) mean square over T
    rel_frame_var = (frame_var / total_msq).mean().item()  # frame-varying energy fraction
    normed = F.normalize(bfc, dim=-1)
    cos = torch.einsum('btgc,bthc->btgh', normed, normed)  # (B,T,G,G)
    g = bfc.shape[2]
    iu = torch.triu_indices(g, g, offset=1)
    cross_branch_cos = cos[:, :, iu[0], iu[1]].mean().item() if g >= 2 else float('nan')
    return {
        'descr_abs_mean': descr_abs_mean,
        'cross_frame_std': cross_frame_std,
        'const_fluct_ratio': ratio,
        'rel_frame_var': rel_frame_var,
        'cross_branch_cos': cross_branch_cos,
    }


def ratr_without_time_centering(loss, branch_feats: torch.Tensor) -> torch.Tensor:
    """Pre-fix baseline: RATRLoss.forward WITHOUT subtracting the temporal mean.

    Reuses the loss module's ``_d_ktau`` and ``_build_negative_sequence`` so the
    only difference vs the fixed loss is the missing time-centering step. This is a
    diagnostic-only replica for an apples-to-apples comparison on the same input.
    """
    bf = branch_feats
    if bf.dim() != 4:
        raise ValueError(f'expected 4D (B,T,G,C), got {tuple(bf.shape)}')
    b, t, g, d = bf.shape
    if g < 2:
        return bf.new_zeros(())
    bf = F.normalize(bf.float(), dim=-1)  # NO time-centering (the bug)
    flat = bf.view(b * t, g, d)
    video_ids = torch.arange(b, device=bf.device).unsqueeze(1).expand(b, t).reshape(-1)
    frame_ids = torch.arange(t, device=bf.device).unsqueeze(0).expand(b, t).reshape(-1)
    sim_mats = [flat[:, gi] @ flat[:, gi].transpose(0, 1) for gi in range(g)]
    pairs = list(combinations(range(g), 2))
    intra, inter = [], []
    for ai in range(b * t):
        av, af = video_ids[ai], frame_ids[ai]
        pos = (video_ids == av) & (torch.abs(frame_ids - af) == 1)
        for lb, rb in pairs:
            if pos.any():
                intra.append(loss._d_ktau(sim_mats[lb][ai, pos], sim_mats[rb][ai, pos]))
            ln = loss._build_negative_sequence(flat, ai, lb, video_ids, frame_ids)
            rn = loss._build_negative_sequence(flat, ai, rb, video_ids, frame_ids)
            if ln is not None and rn is not None:
                inter.append(loss._d_ktau(ln, rn))
    zero = bf.new_zeros(())
    il = torch.stack(intra).mean() if intra else zero
    el = torch.stack(inter).mean() if inter else zero
    return (loss.intra_weight * il + loss.inter_weight * el) * loss.loss_weight


def build_ratr(ratr_opt: dict | None):
    opt = dict(ratr_opt) if ratr_opt else {'type': 'RATRLoss', 'tau': 0.1,
                                           'intra_weight': 1.0, 'inter_weight': 1.0}
    opt.setdefault('type', 'RATRLoss')
    return build_loss(opt)


def _fmt(geo: dict) -> str:
    return (f"descr_abs_mean={geo['descr_abs_mean']:.4f}  "
            f"cross_frame_std={geo['cross_frame_std']:.4f}  "
            f"const:fluct={geo['const_fluct_ratio']:.1f}x  "
            f"rel_frame_var={geo['rel_frame_var']:.4f}  "
            f"cross_branch_cos={geo['cross_branch_cos']:.3f}")


def run_synthetic():
    print('=== RATR diagnostic self-test (synthetic constant-dominated descriptors) ===')
    loss = build_ratr(None)
    torch.manual_seed(0)
    fluct = torch.randn(1, 7, 3, 16)
    const = 10.0 * torch.randn(1, 1, 3, 16).expand(1, 7, 3, 16)
    bfc = (const + fluct).contiguous()
    geo = descriptor_geometry(bfc)
    l_fixed = float(loss(bfc))
    l_buggy = float(ratr_without_time_centering(loss, bfc))
    print(f'  geometry: {_fmt(geo)}')
    print(f'  l_ratr WITHOUT centering (pre-fix): {l_buggy:+.6e}')
    print(f'  l_ratr WITH centering    (fixed)  : {l_fixed:+.6e}')
    ok = abs(l_buggy) < 1e-3 < abs(l_fixed)
    print(f'  => {"PASS" if ok else "FAIL"}: fix recovers signal on constant-dominated input')
    return 0 if ok else 1


def run_real(args):
    os.chdir(OFR_ROOT)
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    opt = load_variant_opt(args.variant)
    exp_name = opt['name']
    ckpt = find_checkpoint(exp_name, args.ckpt)
    ratr_opt = opt.get('train', {}).get('ratr_opt')
    loss = build_ratr(ratr_opt)

    print('=== RATR signal diagnostic (real checkpoint) ===')
    print(f'  variant     : {args.variant} ({exp_name})')
    print(f'  checkpoint  : {os.path.relpath(ckpt, OFR_ROOT)}')
    print(f'  device      : {device}')
    print(f'  num_clips   : {args.num_clips}   num_frames/clip: {args.num_frames}')
    print(f'  ratr_opt    : {ratr_opt}')
    print()

    net = build_net(opt['network_g'], ckpt, device)
    if not hasattr(net, 'get_branch_features'):
        raise RuntimeError('net_g has no get_branch_features(); is use_mgfe enabled?')

    ds_opt = dict(opt['datasets']['val'])
    ds_opt.setdefault('phase', 'val')
    ds_opt.setdefault('scale', 1)
    dataset = build_dataset(ds_opt)
    loader = build_dataloader(dataset, ds_opt, num_gpu=1, dist=False, sampler=None, seed=2021)

    loss_name = type(loss).__name__
    is_ratr = loss_name == 'RATRLoss'
    fixed_vals, buggy_vals, geos = [], [], []
    for clip_idx, data in enumerate(loader):
        if clip_idx >= args.num_clips:
            break
        lq = data['lq']
        if args.num_frames > 0 and lq.size(1) > args.num_frames:
            lq = lq[:, :args.num_frames]
        lq = lq.to(device)
        folder = data.get('folder', [f'clip_{clip_idx}'])[0]
        with torch.no_grad():
            net(lq)
            bfc = net.get_branch_features()
        if bfc is None:
            raise RuntimeError('branch_feats_cache is None after forward; MGFE not engaged.')
        bfc = bfc.float().cpu()
        geo = descriptor_geometry(bfc)
        l_fixed = float(loss(bfc))
        l_buggy = float(ratr_without_time_centering(loss, bfc)) if is_ratr else float('nan')
        geos.append(geo)
        fixed_vals.append(l_fixed)
        buggy_vals.append(l_buggy)
        print(f'  [{clip_idx + 1}/{args.num_clips}] {folder}  bfc={tuple(bfc.shape)}')
        print(f'        {_fmt(geo)}')
        if is_ratr:
            print(f'        l_ratr  pre-fix={l_buggy:+.6e}   fixed={l_fixed:+.6e}')
        else:
            print(f'        {loss_name}={l_fixed:+.6e}  (per-frame branch decorrelation; no time-centering dependence)')

    if not fixed_vals:
        raise RuntimeError('no clips processed; check val dataset paths.')

    n = len(fixed_vals)
    mean_fixed = sum(fixed_vals) / n
    mean_ratio = sum(g['const_fluct_ratio'] for g in geos) / n
    mean_cos = sum(g['cross_branch_cos'] for g in geos) / n
    print()
    print('  ===== SUMMARY =====')
    print(f'  clips={n}  mean const:fluct ratio={mean_ratio:.1f}x  mean cross_branch_cos={mean_cos:.3f}')
    if is_ratr:
        mean_buggy = sum(buggy_vals) / n
        print(f'  mean l_ratr  pre-fix={mean_buggy:+.6e}   fixed={mean_fixed:+.6e}')
        recovered = abs(mean_buggy) < abs(mean_fixed) and abs(mean_fixed) > 1e-3
        print(f'  => {"RECOVERED" if recovered else "NOT RECOVERED"}: '
              f'time-centering fix vs pre-fix on real {args.variant} descriptors')
    else:
        print(f'  mean {loss_name}={mean_fixed:+.6e}  '
              f'(0 => orthogonal branches; grows toward loss_weight as branches collinear)')
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--variant', default='b1', help='variant key, e.g. b1/t1/d1/a3')
    parser.add_argument('--num_clips', type=int, default=3)
    parser.add_argument('--num_frames', type=int, default=7,
                        help='frames per clip to match training (0 = whole clip)')
    parser.add_argument('--ckpt', default=None, help='checkpoint path override')
    parser.add_argument('--synthetic', action='store_true',
                        help='self-test on synthetic descriptors (no ckpt/GPU)')
    args = parser.parse_args()
    sys.exit(run_synthetic() if args.synthetic else run_real(args))


if __name__ == '__main__':
    main()
