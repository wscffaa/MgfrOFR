# F1 Average-Fusion Freeze - 2026-07-01

Scope: `001-reidmamba` Symmetry round-1 rework package.

## Decision

The submitted MgfrOFR model is F1: MGFE + RATR with average restoration-token fusion. A3 remains only the max-fusion ablation control.

## Protocol

| Dataset | Test config | Fusion | Checkpoint |
|---|---|---|---|
| REDS_synthetic | `projects/001-reidmamba/Exp/options/test/mgfrofr_f1_synthetic.yml` | `avg` | `projects/001-reidmamba/Exp/experiments/mgfrofr_f1_avg/models/net_g_80000.pth` |
| DAVIS_synthetic | `projects/001-reidmamba/Exp/options/test/mgfrofr_f1_davis.yml` | `avg` | `projects/001-reidmamba/Exp/experiments/mgfrofr_f1_avg/models/net_g_80000.pth` |
| RealFilm_SRWOV | `projects/001-reidmamba/Exp/options/test/mgfrofr_f1_realworld.yml` | `avg` | `projects/001-reidmamba/Exp/experiments/mgfrofr_f1_avg/models/net_g_80000.pth` |

The checkpoint is the best-selected F1 checkpoint for the current paper protocol. The path is explicit in the test YAMLs; no hidden checkpoint fallback is used.

## Frozen Metrics

| Dataset | PSNR | SSIM | LPIPS | DISTS |
|---|---:|---:|---:|---:|
| REDS_synthetic | 27.8615 | 0.9255 | 0.0600 | 0.0656 |
| DAVIS_synthetic | 26.5488 | 0.9064 | 0.0891 | 0.0883 |

| Dataset | NIQE | BRISQUE | CLIP-IQA+ |
|---|---:|---:|---:|
| RealFilm_SRWOV | 5.1233 | 24.7942 | 0.4092 |

## Source Map

| Evidence | Source |
|---|---|
| Model-selection status | `projects/001-reidmamba/Exp/registry.yaml`, `paper_model_selection.main_model: F1` |
| F1 metric record | `projects/001-reidmamba/Exp/registry.yaml`, F1 `test_results` |
| SOTA metric record | `projects/001-reidmamba/Exp/metrics.yaml`, `sota.synthetic` and `sota.realworld` |
| Paired REDS evidence | `projects/001-reidmamba/Paper/writing/review/round1/t5-figures/evidence/per_clip_f1_vs_a0_reds_synthetic_20260630.json` |
| REDS F1 raw source log | `projects/001-reidmamba/Exp/results/mgfrofr_f1_synthetic/test_mgfrofr_f1_synthetic_20260626_093612.log` on `A100_22_aliyun` |

## REDS Paired Statistics

F1 vs A0 under the same 30-clip REDS_synthetic protocol:

| Metric | Mean A0 | Mean F1 | Paired direction | Wilcoxon p |
|---|---:|---:|---|---:|
| PSNR | 26.8403 | 27.8615 | higher is better | 3.73e-9 |
| SSIM | 0.9153 | 0.9255 | higher is better | 1.73e-6 |
| LPIPS | 0.0719 | 0.0600 | lower is better | 1.86e-9 |
| DISTS | 0.0733 | 0.0656 | lower is better | 1.92e-6 |

## Manuscript Policy

- Main model wording must say average fusion, not max fusion.
- A3 must be described only as the max-fusion ablation control.
- RealFilm claims must not say MgfrOFR improves CLIP-IQA+ over MambaOFR; F1 is lower on CLIP-IQA+ and should be framed as a naturalness-versus-enhancement trade-off.
- DAVIS_synthetic is freeze evidence for protocol completeness; do not invent cross-method DAVIS rankings unless baseline DAVIS rows are explicitly sourced.
