# Fig. 9a Branch-Similarity Provenance

## Purpose

This file records the data source and rendering command for the revised Fig. 9a branch-balance evidence in the round-2 Symmetry package.

## Source Data

- MGFE-only input JSON: `projects/001-reidmamba/Paper/writing/review/round1/t5-figures/evidence/branch_sim_evolution_a1_20260630.json`
- Full MgfrOFR input JSON: `projects/001-reidmamba/Paper/writing/review/round1/t5-figures/evidence/branch_sim_evolution_f1_20260630.json`
- Archived copies in this round-2 package:
  - `evidence/fig9a_branch_sim_evolution_a1_realdata_20260630.json`
  - `evidence/fig9a_branch_sim_evolution_f1_realdata_20260630.json`

## Protocol

- Dataset field: `synthetic`
- Number of clips: `30`
- Metric field: `mean_offdiagonal_cosine_similarity(branch_sim_bwd+fwd)`
- Checkpoints: `50K`, `100K`, `150K`, `200K`
- Compared variants:
  - `a1`: MGFE-only configuration
  - `f1`: full MgfrOFR model

## Render Command

```bash
.venv-vs/bin/python3 projects/001-reidmamba/Paper/symmetry/03_revision_round2_rework/scripts/render_fig9a_branch_similarity_realdata.py
```

## Outputs

- Manuscript figure: `source/figures/Fig9a_branch_similarity.pdf`
- Preview image: `evidence/Fig9a_branch_similarity_realdata_preview.png`
- Machine-readable summary: `evidence/fig9a_branch_similarity_realdata_summary.json`

## Final 200K Values

- MGFE-only mean off-diagonal similarity: `0.8625233620 +/- 0.0055844120`
- Full MgfrOFR mean off-diagonal similarity: `0.2608974052 +/- 0.1434501357`
- MGFE-only final off-diagonal matrix range: `0.8456009318--0.8958926270`
- Full MgfrOFR final off-diagonal matrix range: `0.2261024829--0.3102188795`

