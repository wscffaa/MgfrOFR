"""Find frames where A3 most outperforms A0 by per-frame PSNR difference."""
import os
import numpy as np
from PIL import Image
import csv

results_root = '/mnt/data/Antigravity_OFR/projects/015-reidmamba/Exp/results_best'
gt_root = '/mnt/data/Antigravity_OFR/datasets/OldFilmRestoration/val/REDS/GT/val_sharp'
lq_root = '/mnt/data/Antigravity_OFR/datasets/OldFilmRestoration/val/REDS/LQ/val_sharp_degraded'

a0_dir = os.path.join(results_root, 'mgfrofr_a0_synthetic_best/visualization/REDS_synthetic')
a3_dir = os.path.join(results_root, 'mgfrofr_a3_synthetic_best/visualization/REDS_synthetic')

def psnr(img1, img2):
    mse = np.mean((img1.astype(float) - img2.astype(float)) ** 2)
    if mse == 0:
        return 100.0
    return 10 * np.log10(255.0 ** 2 / mse)

def degradation_score(lq, gt):
    return np.abs(lq.astype(float) - gt.astype(float)).mean()

results = []
clips = sorted(os.listdir(a0_dir))
print(f"Scanning {len(clips)} clips...")

for clip in clips:
    a0_out_dir = os.path.join(a0_dir, clip, 'outputs')
    a3_out_dir = os.path.join(a3_dir, clip, 'outputs')
    gt_clip = os.path.join(gt_root, clip)
    lq_clip = os.path.join(lq_root, clip)

    if not all(os.path.isdir(d) for d in [a0_out_dir, a3_out_dir, gt_clip, lq_clip]):
        continue

    a0_files = sorted([f for f in os.listdir(a0_out_dir) if f.endswith('.png')])

    for a0_file in a0_files:
        frame_id = a0_file.split('_')[0]
        a3_file = f"{frame_id}_mgfrofr_a3_synthetic_best.png"
        gt_file = f"{frame_id}.png"

        a0_path = os.path.join(a0_out_dir, a0_file)
        a3_path = os.path.join(a3_out_dir, a3_file)
        gt_path = os.path.join(gt_clip, gt_file)
        lq_path = os.path.join(lq_clip, gt_file)

        if not all(os.path.exists(p) for p in [a0_path, a3_path, gt_path, lq_path]):
            continue

        a0_img = np.array(Image.open(a0_path))
        a3_img = np.array(Image.open(a3_path))
        gt_img = np.array(Image.open(gt_path).resize(
            (a0_img.shape[1], a0_img.shape[0]), Image.LANCZOS))
        lq_img = np.array(Image.open(lq_path).resize(
            (a0_img.shape[1], a0_img.shape[0]), Image.LANCZOS))

        p0 = psnr(a0_img, gt_img)
        p3 = psnr(a3_img, gt_img)
        delta = p3 - p0
        deg = degradation_score(lq_img, gt_img)

        results.append({
            'clip': clip, 'frame': frame_id,
            'psnr_a0': round(p0, 4), 'psnr_a3': round(p3, 4),
            'delta_psnr': round(delta, 4), 'degradation': round(deg, 4),
        })

    print(f"  {clip}: {len(a0_files)} frames")

results.sort(key=lambda x: x['delta_psnr'], reverse=True)

out_csv = '/mnt/data/Antigravity_OFR/projects/001-reidmamba/Exp/vis_output/frame_ranking.csv'
with open(out_csv, 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['clip','frame','psnr_a0','psnr_a3','delta_psnr','degradation'])
    w.writeheader()
    w.writerows(results)

print(f"\n=== Top 10 frames where A3 beats A0 ===")
for r in results[:10]:
    print(f"  clip={r['clip']} frame={r['frame']} "
          f"PSNR A0={r['psnr_a0']:.2f} A3={r['psnr_a3']:.2f} "
          f"Δ={r['delta_psnr']:+.2f} deg={r['degradation']:.2f}")

print(f"\nSaved {len(results)} rows to {out_csv}")
