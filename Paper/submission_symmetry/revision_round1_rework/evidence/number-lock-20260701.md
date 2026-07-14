# Number Lock - 2026-07-01

Scope: `001-reidmamba` Symmetry round-1 rework package.

Authoritative source:
- `projects/001-reidmamba/Exp/metrics.yaml`, `sota.synthetic`, `sota.realworld`, and F1 ablation blocks.
- `projects/001-reidmamba/Exp/registry.yaml`, F1 `test_results` block.
- `projects/001-reidmamba/Exp/options/test/mgfrofr_f1_{synthetic,davis,realworld}.yml`, explicit F1 average-fusion protocol and checkpoint path.
- `projects/001-reidmamba/Paper/writing/review/round1/t5-figures/evidence/per_clip_f1_vs_a0_reds_synthetic_20260630.json`, paired F1/A0 per-clip statistics.

Frozen manuscript values:

| Context | Method | PSNR | SSIM | LPIPS | DISTS |
|---|---:|---:|---:|---:|---:|
| REDS_synthetic | MambaOFR | 26.84 | 0.9153 | 0.0719 | 0.0733 |
| REDS_synthetic | MgfrOFR/F1 average fusion | 27.86 | 0.9255 | 0.0600 | 0.0656 |
| DAVIS_synthetic | MgfrOFR/F1 average fusion | 26.55 | 0.9064 | 0.0891 | 0.0883 |

| Context | Method | NIQE | BRISQUE | CLIP-IQA+ |
|---|---:|---:|---:|---:|
| SRWOV real | OldPhoto | 6.56 | 30.45 | 0.4503 |
| SRWOV real | RTN | 5.17 | 19.00 | 0.4163 |
| SRWOV real | MambaOFR | 5.34 | 29.79 | 0.4351 |
| SRWOV real | MgfrOFR/F1 average fusion | 5.12 | 24.79 | 0.4092 |

Manuscript policy:
- Main SOTA and real-world comparison text must cite these frozen F1 average-fusion values.
- Project-internal ablation and sensitivity tables may keep their own protocol-specific values, but they must not override the frozen main comparison values.
- The selected checkpoint is `projects/001-reidmamba/Exp/experiments/mgfrofr_f1_avg/models/net_g_80000.pth`, explicitly referenced by all three F1 test YAMLs.
- Wilcoxon text is supporting evidence only. Under the frozen F1/A0 protocol, PSNR, SSIM, LPIPS, and DISTS are all significant; report the paired-test p-values from the per-clip JSON.
