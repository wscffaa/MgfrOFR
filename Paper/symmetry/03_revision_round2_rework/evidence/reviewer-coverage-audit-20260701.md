# Reviewer Coverage Audit

Scope: `revision_round1_rework` upload candidate, verified on 2026-07-01.

Verdict: all reviewer comments are answered by the current response letters and final manuscript/source package. The supplementary video that Reviewer 1 suggested as an optional improvement is now provided as Supplementary Video S1; local package gates pass.

## Validation signals

- Clean manuscript: `upload/MGFROFR-clean.pdf`, 27 pages.
- Highlighted changes: `upload/MGFROFR-highlighted-changes.pdf`, 27 pages, generated from byte-reproducible `latexpand --empty-comments` flats against `symmetry/01_initial_submission/source/` using `latexdiff --no-del --graphics-markup=none`.
- Independent source-zip rebuild: `upload/MGFROFR-latex-source.zip`, 27 pages after extraction to a clean temp dir.
- Supplementary video: `upload/Supplementary_Video_S1.mp4`, H.264/yuv420p MP4, 20,655,713 bytes, 37.4 s (part 1 REDS-synthetic with GT and per-frame PSNR; part 2 real-world SRWOV with overall NIQE/BRISQUE).
- Final TeX log gate: rerun after the layout adjustment and highlighted-diff refresh; no matches for LaTeX errors, unresolved references, unresolved citations, missing files, rerun warnings, or misplaced alignment errors in the clean and highlighted source logs.
- Response DOCX validation: `officecli validate` passed for both reviewer response files.
- Visual spot check: rendered clean PDF pages 16--18; Figure 4 now shares page 16 with Ablation Study text and Table 3, and the following figure/table pages fit without overlap.

## Reviewer 1

| ID | Reviewer asked for | Current evidence | Status |
|---|---|---|---|
| R1-C1 | Clarify novelty over MambaOFR and recent multi-scale/token/Mamba methods. | Introduction positions representation-level symmetry and MGFE/RATR at `MGFROFR-new-flat.tex:85-98`; Related Work distinguishes old film restoration, SSM, multi-branch, and ranking regularization at `MGFROFR-new-flat.tex:107-133`; Discussion summarizes the MambaOFR differences at `MGFROFR-new-flat.tex:715-719`. | OK |
| R1-C2 | Explain fairness/reproducibility, retraining, hyperparameters, degradation adaptation, and baseline status. | Baseline protocol at `MGFROFR-new-flat.tex:532-540`; metrics/datasets/protocol at `MGFROFR-new-flat.tex:500-517`; response limits token-insertion and branch-aggregation controls to measured scope. | OK |
| R1-C3 | Complete ablation: token insertion, fusion choice, ranking metric, branch aggregation, diversity loss. | Average-fusion method correction at `MGFROFR-new-flat.tex:224-258`; max-fusion control at `MGFROFR-new-flat.tex:628-647`; descriptive sensitivity/control rows at `MGFROFR-new-flat.tex:658-680`; response uses measured-scope language for additional controls. | OK |
| R1-C4 | Make qualitative ROI comparisons clearer and consider supplementary video. | Full-method Figure 4/5 captions and discussion; Supplementary Video S1 (two-part: REDS-synthetic with GT and per-frame PSNR, then real-world SRWOV with overall NIQE/BRISQUE) is included, referenced in `results.tex`, and declared in `\supplementary{}`; both response letters state the video is provided. | OK |
| R1-C5 | Add practical complexity: runtime, memory, params, FPS, comparison against baselines. | Complexity protocol and table at `MGFROFR-new-flat.tex:687-705`; response reports the MgfrOFR row values and provenance. | OK |
| R1-C6 | Strengthen limitations and failure-case discussion. | Trade-off and failure discussion at `MGFROFR-new-flat.tex:724-769`; conclusion limitations at `MGFROFR-new-flat.tex:776-778`; no unsupported Figure 10 claim remains. | OK |

## Reviewer 2

| ID | Reviewer asked for | Current evidence | Status |
|---|---|---|---|
| R2-C1 | Tie representation symmetry more tightly to Symmetry journal scope. | Representation-level framing in Introduction at `MGFROFR-new-flat.tex:85-98`; symmetry-specific related work at `MGFROFR-new-flat.tex:131-133`; scope narrowing in Discussion at `MGFROFR-new-flat.tex:715-719`. | OK |
| R2-C2 | Provide more direct RATR evidence, not only indirect metrics. | Branch-similarity and error-map evidence at `MGFROFR-new-flat.tex:733-751`; response only claims Figures 9a/9b, matching the final source package. | OK |
| R2-C3 | Discuss why MGFE-only improves fidelity but is weaker on LPIPS/DISTS, and how RATR mitigates it. | Ablation discussion at `MGFROFR-new-flat.tex:647`; perception-distortion explanation at `MGFROFR-new-flat.tex:724-726`. | OK |
| R2-C4 | Add sensitivity for branch/token choices and support computational overhead. | Granularity, token-insertion, and branch-aggregation controls at `MGFROFR-new-flat.tex:658-680`; complexity evidence at `MGFROFR-new-flat.tex:687-705`; limitation notes training-time cost at `MGFROFR-new-flat.tex:767`. | OK |
| R2-C5 | Improve reproducibility: token initialization, insertion implementation, hyperparameters, code availability. | Token definition, truncated-normal initialization, and insertion operator at `MGFROFR-new-flat.tex:224-230`; implementation protocol at `MGFROFR-new-flat.tex:500-540`; code availability at `MGFROFR-new-flat.tex:792`; implementation source initializes tokens with `trunc_normal_(std=0.02)` at `projects/001-reidmamba/archs/mgfe.py:52-53`. | OK |
| R2-C6 | Shorten Introduction and make terminology consistent. | Introduction now gives a compact motivation and four contributions at `MGFROFR-new-flat.tex:85-98`; response states proofreading was done after finalizing quantitative values. | OK |
| R2-C7 | Clarify Eq. 14 modulation, justify two-neighbor ranking signal, and extend significance testing to LPIPS/DISTS. | 10% modulation explanation at `MGFROFR-new-flat.tex:317-321`; temporal-neighbor justification at `MGFROFR-new-flat.tex:357-367`; paired MgfrOFR-vs.-MambaOFR Wilcoxon tests report significance for PSNR, SSIM, LPIPS, and DISTS. | OK |
| R2-C8 | Enlarge ROI regions in Figures 4 and 5. | Page-width qualitative captions and full-method layout at `MGFROFR-new-flat.tex:603-620`; rendered pages were visually checked. | OK |
| R2-C9 | Check reference formatting under MDPI guidelines. | Final `latexmk` source-zip rebuild uses `Definitions/mdpi.bst` and final log gate reports no unresolved citations or bibliography warnings; bibliography is included via `MGFROFR-new-flat.tex:825`. | OK |
| R2-C10 | Proofread for terminology consistency, repetition, and long sentences. | Response letter records proofreading after finalizing quantitative values; final TeX/DOCX validation passed. | OK |

## Residual risk

- None outstanding. The previously advisory supplementary video is now provided as Supplementary Video S1 (H.264 MP4, 20,655,713 bytes, two-part: synthetic PSNR + real-world NR), referenced in the manuscript and declared in `\supplementary{}`, and both response letters state it is included.
