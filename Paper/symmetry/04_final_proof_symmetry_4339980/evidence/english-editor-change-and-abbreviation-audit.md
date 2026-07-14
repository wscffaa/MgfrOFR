# English Editor Change and Abbreviation Audit

## Instruction under review

The proof was checked against the editor instruction to preserve intended meaning and to define abbreviations/acronyms independently at first appearance in the abstract, the main text, and the first affected figure or table.

## Verdict

`PASS` for semantic retention and all three abbreviation scopes.

## Semantic comparison

- Formal numeric token gate: `953/953`, exact order, sequence SHA-256 `887fde3997c87bbe025f778cb37fa302a37dd67cfd076cd86265d7fd6dcfcf7c`.
- Equation gate: all 27 equation bodies byte-exact, combined SHA-256 `92c8735aafb24b8a792aaea462e62df38bcf69d6a594c1ade51481e7a6ce9f79`.
- Structure gate: 8 figures, 5 tables, 8 figure labels, 5 table labels, 9 equation labels, and 34 section labels retain count and order.
- Provenance gate: 8 image paths, 93 citation commands, and 101 citation keys retain exact order; Figures, Definitions, and `references.bib` assets are unchanged.
- The compact contribution-summary sentence retains SRWOV synthetic/real-world coverage, statistical tests, ablations, complexity analysis, fidelity, naturalness, and the relative `modest additional computational cost` claim.

## Three independent abbreviation scopes

| Scope | First-use closure |
|---|---|
| Abstract | Defines Multi-Granularity Feature Decomposition with Ranking-Aware Regularization for Old Film Restoration (MgfrOFR) and Synthetic/Real-World Old Video (SRWOV). |
| Main text | Defines the non-proper-name method, module, metric, dataset, hardware, and software acronyms at their first main-text use, including RTN/RRTN, EDVR/VRT/RVRT, HRNet/PCB/MGN, AI, VGG, CUDA, DAVIS, ROI, and GT. |
| First figure/table | Figure 1 defines MgfrOFR/MGFE/RATR/SSM/DPB/DCN and explains Concat; Table 1 defines its methods and metrics; Table 2 defines its no-reference metrics; Figure 4 defines REDS/ROI/GT; Table 5 defines FP32/FLOPs/FPS and units; Figure 8 defines MAE/GT. |

Stylized model names that are not abbreviations are retained as proper method names.

## Query and rendering checks

- Production comments: `23 %MDPI / 23 %Author / 0 orphan`.
- Original highlights retained: `53 \hl{}`; final source has `3 \highlighting{}`.
- PDF comment leakage: zero `%MDPI`, `%Author`, general-note, TODO, TBD, or FIXME strings.
- Final PDF: 28 A4 pages; no clipping, overlap, blank page, cross-figure sentence split, unreadable label, or non-link annotation.
- Maximum non-exempt blank band: `24.8%`; page 25 back-matter transition is an indivisible-block exemption.

## Final artifact identity

- TeX SHA-256: `d5e685c98c61a7432615d415ee8b55e9cbfb531fc575e5877f6ad16386be1d8b`.
- Upload ZIP SHA-256: `4152460d8e7252c4324582b5b03b3c30efc7015a0ce4029c09d939f64ac85696`.
- Independently rebuilt upload PDF SHA-256: `7f33ec06185060db77868514a47d8b279ce10f4679173ddb09ba37afc5ec9c4c`.

