#!/usr/bin/env python3
"""
Frame Ranker: 批量计算逐帧 PSNR/SSIM，按方法间差异排序输出 top-N 帧。

支持两种目录结构:
  A) 多 clip 结构: gt_dir/clip_XXX/XXXXXXXX.png
  B) 扁平结构: gt_dir/XXXXXXXX.png

Usage:
  # 比较 A0 和 A3，找 A3 显著优于 A0 的帧
  python frame_ranker.py \
    --gt /path/to/gt \
    --methods a0:/path/to/a0,a3:/path/to/a3 \
    --baseline a0 --target a3 \
    --output ranking.json

  # 也可以只算一个方法的指标
  python frame_ranker.py \
    --gt /path/to/gt \
    --methods a3:/path/to/a3 \
    --output metrics.json
"""

import argparse
import json
import os
import sys
from pathlib import Path

import numpy as np
from PIL import Image


def calc_psnr(img1: np.ndarray, img2: np.ndarray, max_val: float = 255.0) -> float:
    mse = np.mean((img1.astype(np.float64) - img2.astype(np.float64)) ** 2)
    if mse == 0:
        return float('inf')
    return 10.0 * np.log10(max_val ** 2 / mse)


def calc_ssim(img1: np.ndarray, img2: np.ndarray) -> float:
    try:
        from skimage.metrics import structural_similarity
        if img1.ndim == 3:
            return structural_similarity(img1, img2, channel_axis=2, data_range=255)
        return structural_similarity(img1, img2, data_range=255)
    except ImportError:
        return -1.0


def load_and_resize(path: str, target_size: tuple = None) -> np.ndarray:
    img = Image.open(path).convert('RGB')
    if target_size and img.size != target_size:
        img = img.resize(target_size, Image.BICUBIC)
    return np.array(img)


def discover_frames(root_dir: str, output_only: bool = True) -> list:
    """Discover all frames, returns list of (relative_path, absolute_path).

    If output_only=True, skip files under 'features'/'masks'/'flow' subdirs
    (only keep files in 'outputs' or direct children).
    """
    root = Path(root_dir)
    img_exts = {'.png', '.jpg', '.jpeg', '.bmp', '.tiff'}
    skip_dirs = {'features', 'masks', 'flow', 'tb_logger', '__pycache__'}
    frames = []
    for f in sorted(root.rglob('*')):
        if f.suffix.lower() in img_exts and f.is_file():
            rel = f.relative_to(root)
            if output_only and any(part in skip_dirs for part in rel.parts):
                continue
            frames.append((str(rel), str(f)))
    return frames


def _extract_frame_key(rel_path: str) -> str:
    """Extract a canonical frame key for alignment.

    Handles:
      - GT: '000/00000000.png' -> '000/00000000'
      - Method: '000/outputs/00000000_mgfrofr_a0_synthetic_best.png' -> '000/00000000'
    """
    p = Path(rel_path)
    stem = p.stem

    import re
    match = re.match(r'^(\d{6,8})', stem)
    frame_id = match.group(1) if match else stem

    parts = p.parts
    clip_parts = [part for part in parts[:-1]
                  if part not in ('outputs', 'features', 'masks', 'flow', 'visualization')]
    if clip_parts:
        return '/'.join(clip_parts) + '/' + frame_id
    return frame_id


def align_frames(gt_frames: list, method_frames: dict) -> list:
    """Align frames across GT and all methods by frame key (clip + frame number)."""
    gt_by_key = {}
    for rel, abspath in gt_frames:
        key = _extract_frame_key(rel)
        gt_by_key[key] = (rel, abspath)

    method_by_key = {}
    for name, m_frames in method_frames.items():
        m_dict = {}
        for mrel, mabs in m_frames:
            key = _extract_frame_key(mrel)
            m_dict[key] = mabs
        method_by_key[name] = m_dict

    aligned = []
    for key in sorted(gt_by_key.keys()):
        gt_rel, gt_abs = gt_by_key[key]
        entry = {'gt_rel': gt_rel, 'gt_abs': gt_abs, 'methods': {}}
        all_found = True
        for name in method_frames.keys():
            m_path = method_by_key[name].get(key)
            if m_path:
                entry['methods'][name] = m_path
            else:
                all_found = False
                break
        if all_found and entry['methods']:
            aligned.append(entry)
    return aligned


def rank_frames(gt_dir: str, methods: dict, baseline: str = None,
                target: str = None, lq_dir: str = None,
                min_degradation: float = 0.0) -> list:
    """
    Compute per-frame metrics and rank.

    Args:
        gt_dir: GT directory
        methods: {name: dir_path}
        baseline: baseline method name (for delta computation)
        target: target method name
        lq_dir: LQ input directory (for degradation filtering)
        min_degradation: minimum |LQ-GT| MSE to include frame

    Returns:
        List of frame entries sorted by delta_psnr (descending)
    """
    gt_frames = discover_frames(gt_dir)
    method_frames = {name: discover_frames(d) for name, d in methods.items()}
    aligned = align_frames(gt_frames, method_frames)

    if not aligned:
        print(f"[ERROR] No aligned frames found. GT has {len(gt_frames)} frames.")
        for name, frames in method_frames.items():
            print(f"  {name}: {len(frames)} frames")
        return []

    gt_sample = load_and_resize(aligned[0]['gt_abs'])
    gt_size = (gt_sample.shape[1], gt_sample.shape[0])

    method_names = list(methods.keys())
    first_method_sample = load_and_resize(list(aligned[0]['methods'].values())[0])
    method_size = (first_method_sample.shape[1], first_method_sample.shape[0])

    resize_gt = gt_size != method_size
    if resize_gt:
        print(f"[INFO] GT size {gt_size} != method size {method_size}, will resize GT for comparison")

    results = []
    total = len(aligned)
    for i, entry in enumerate(aligned):
        if (i + 1) % 50 == 0 or i == 0:
            print(f"  Processing frame {i+1}/{total}...")

        gt_img = load_and_resize(entry['gt_abs'],
                                 method_size if resize_gt else None)

        frame_result = {
            'rel_path': entry['gt_rel'],
            'gt_abs': entry['gt_abs'],
            'metrics': {}
        }

        if lq_dir:
            lq_path = os.path.join(lq_dir, entry['gt_rel'])
            if os.path.exists(lq_path):
                lq_img = load_and_resize(lq_path, method_size if resize_gt else None)
                deg_mse = np.mean((lq_img.astype(float) - gt_img.astype(float)) ** 2)
                frame_result['degradation_mse'] = float(deg_mse)
                if deg_mse < min_degradation:
                    continue

        for name in method_names:
            m_path = entry['methods'][name]
            m_img = load_and_resize(m_path)

            if m_img.shape != gt_img.shape:
                m_pil = Image.fromarray(m_img)
                m_pil = m_pil.resize((gt_img.shape[1], gt_img.shape[0]), Image.BICUBIC)
                m_img = np.array(m_pil)

            psnr = calc_psnr(m_img, gt_img)
            ssim = calc_ssim(m_img, gt_img)

            frame_result['metrics'][name] = {
                'psnr': round(psnr, 4),
                'ssim': round(ssim, 4),
                'path': m_path
            }

        if baseline and target:
            b_psnr = frame_result['metrics'].get(baseline, {}).get('psnr', 0)
            t_psnr = frame_result['metrics'].get(target, {}).get('psnr', 0)
            frame_result['delta_psnr'] = round(t_psnr - b_psnr, 4)
        else:
            first_method = method_names[0]
            frame_result['delta_psnr'] = frame_result['metrics'][first_method]['psnr']

        results.append(frame_result)

    results.sort(key=lambda x: x['delta_psnr'], reverse=True)
    return results


def main():
    parser = argparse.ArgumentParser(description='Frame Ranker for OFR paper visualization')
    parser.add_argument('--gt', required=True, help='GT directory')
    parser.add_argument('--methods', required=True,
                        help='Methods in name:path format, comma-separated. '
                             'e.g., a0:/path/to/a0,a3:/path/to/a3')
    parser.add_argument('--baseline', default=None, help='Baseline method name')
    parser.add_argument('--target', default=None, help='Target method name')
    parser.add_argument('--lq', default=None, help='LQ input directory (for degradation filtering)')
    parser.add_argument('--min-degradation', type=float, default=0.0,
                        help='Minimum degradation MSE to include a frame')
    parser.add_argument('--top', type=int, default=20, help='Number of top frames to output')
    parser.add_argument('--output', required=True, help='Output JSON path')
    args = parser.parse_args()

    methods = {}
    for item in args.methods.split(','):
        name, path = item.split(':', 1)
        methods[name.strip()] = path.strip()

    print(f"[Frame Ranker] GT: {args.gt}")
    for name, path in methods.items():
        print(f"  Method '{name}': {path}")
    if args.baseline and args.target:
        print(f"  Ranking by ΔPSNR = PSNR({args.target}) - PSNR({args.baseline})")

    results = rank_frames(
        gt_dir=args.gt,
        methods=methods,
        baseline=args.baseline,
        target=args.target,
        lq_dir=args.lq,
        min_degradation=args.min_degradation
    )

    top_results = results[:args.top]

    output = {
        'config': {
            'gt_dir': args.gt,
            'methods': methods,
            'baseline': args.baseline,
            'target': args.target,
            'total_frames': len(results),
            'top_n': args.top,
        },
        'frames': top_results
    }

    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    with open(args.output, 'w') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\n[Results] Total aligned frames: {len(results)}")
    print(f"[Results] Top {min(args.top, len(results))} frames saved to {args.output}")
    if top_results:
        print("\nTop 5 frames:")
        for i, r in enumerate(top_results[:5]):
            delta = r.get('delta_psnr', 0)
            m_str = ', '.join(f"{k}: {v['psnr']:.2f}dB" for k, v in r['metrics'].items())
            print(f"  #{i+1} {r['rel_path']} | Δ={delta:+.2f}dB | {m_str}")


if __name__ == '__main__':
    main()
