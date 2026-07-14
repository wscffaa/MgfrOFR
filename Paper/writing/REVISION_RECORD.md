# REVISION_RECORD.md

## Executive Summary

This revision polishes the manuscript as a language, logic, and reviewer-readability edit. The central claim was narrowed to the evidence supported by the current manuscript: MgfrOFR improves old film restoration by balancing coarse-to-fine feature branches with ranking-aware regularization. The revision improves paragraph openings, transitions, statistical wording, no-reference metric interpretation, and method readability while preserving the experimental record.

No numerical results, citations, labels, equations, figure paths, author metadata, bibliography keys, table values, p-values, FLOPs, parameters, memory, speed, PSNR, SSIM, LPIPS, DISTS, NIQE, BRISQUE, or CLIP-IQA+ values were changed. No training-dynamics or convergence figure/section was reintroduced. `Fig7_sensitivity_analysis.png` and `fig:sensitivity` were preserved.

## Five Highest-Impact Original Writing Issues

1. **Symmetry framing was too broad in places.** The revision makes clear that symmetry is used in a limited representation-level sense, not as a general mathematical theory or object-level geometric constraint.
2. **The evidence chain needed clearer staging.** The Introduction now moves from old-film degradation, to the gap in single-stream propagation, to MGFE/RATR, and then to the evaluation evidence.
3. **Some results language risked overgeneralization.** Claims based on no-reference metrics are now explicitly limited to statistical naturalness or metric-based perceptual quality.
4. **Statistical wording needed precision.** The Wilcoxon test is now described as testing the zero median paired difference of per-clip means, rather than an imprecise equality of means.
5. **The Methods section was dense and repetitive.** MGFE, RATR, the baseline interface, and the training objective are now described with clearer role separation and reviewer-facing transitions, while the mathematical definitions are preserved.

## File-by-File Changes

| File | Change Type | Summary |
|---|---:|---|
| `sections/abstract.tex` | Wording tightened | Rewritten for concision, clearer method/evidence summary, and a narrower final claim. No numbers or citations were added. |
| `sections/introduction.tex` | Wording tightened | Reorganized task challenge, gap, proposed components, and contributions. Representation-level symmetry is explicitly scoped. |
| `sections/related_work.tex` | Wording tightened | Improved grouping across OFR, SSMs, multi-branch representations, ranking regularization, and representation symmetry. No citations were added or removed. |
| `sections/method.tex` | Wording tightened | Clarified the baseline interface, MGFE token flow, recalibration, RATR ranking construction, and training objective. Equations and labels were preserved. |
| `sections/results.tex` | Wording tightened | Strengthened claim-evidence alignment for Tables `tab:sota`, `tab:realworld`, `tab:ablation`, sensitivity tables, and `tab:complexity`. Statistical claims were made more precise. |
| `sections/discussion.tex` | Wording tightened | Reduced repetition of Results, narrowed the symmetry claim, clarified branch-balance interpretation, and made limitations more explicit. |
| `sections/conclusion.tex` | Wording tightened | Summarized contribution and evidence without overclaiming; limitations are stated as part of the conclusion. |
| `MGFROFR.tex` | Not edited | Main MDPI wrapper, metadata, inputs, keywords, author contributions, funding, data availability, acknowledgments, conflicts, abbreviations, and bibliography commands were preserved. |
| `sections/authors.tex` | Not edited | Author names, affiliations, ORCID commands, and correspondence were preserved. |
| `references.bib` | Not edited | Bibliography keys and entries were preserved. |
| `Definitions/` | Not edited | MDPI class/style files and logos were preserved. |
| `figures/` | Not edited | All figure files and paths were preserved. |
| `REVISION_RECORD.md` | Added | Documents this revision and audit. |
| `polish_changes.diff` | Added | Unified diff patch against the uploaded source package. |

## Section-by-Section Rationale

### Abstract
The abstract was tightened to state the problem, method, training-time regularization, and evidence in a compact sequence. Metric evidence is stated without adding new numbers. The final sentence now states the narrow supported claim.

### Introduction
The Introduction now opens each paragraph with a clear message: old-film degradation is multi-scale; existing OFR propagation mixes cues; the missing piece is OFR-specific granularity separation plus diversity regularization; MgfrOFR addresses this gap. The contribution list was revised to avoid promotional phrasing and to align directly with method and evaluation evidence.

### Related Work
The Related Work section now uses clearer transitions between OFR, general video restoration, state space models, multi-branch representations, diversity/ranking regularization, and representation symmetry. The citation set was preserved exactly.

### Methods
The Methods section was revised for readability while preserving all equations, symbols, labels, algorithm logic, and figure paths. The baseline interface is stated before MGFE details; MGFE's token insertion, progressive fusion, branch mixers, and recalibration are explained in a more linear order; RATR is framed as a training-time branch-balance regularizer rather than an inference module.

### Experiment/Results
The Results section now ties each claim to a table or figure. Statistical claims are limited to the metrics that reach significance. No-reference real-world results are described as statistical naturalness and metric-based perceptual evidence, not as proof of ground-truth fidelity.

### Discussion
The Discussion now separates baseline comparison, module synergy, branch-balance analysis, failure cases, threats to validity, and future work. It avoids turning the paper into a general theory of symmetry and keeps the interpretation tied to MGFE/RATR and the reported figures/tables.

### Conclusion
The Conclusion now summarizes the contribution, synthetic and real-world evidence, ablation evidence, and limitations without overclaiming. It keeps the method's implication focused on coarse-to-fine feature branch balance for old film restoration.

## Claim-Evidence Checks

| Factual or Experimental Claim | Evidence in Manuscript | Status |
|---|---|---:|
| Old film degradation includes scratches, dust, blotches, flicker, blur, grain, and fading. | Introduction and Related Work citations to OFR literature. | Wording tightened |
| Symmetry is used as a representation-level balance concept, not object-level geometry. | Introduction, Related Work, Discussion. | Wording tightened |
| MgfrOFR augments MambaOFR rather than replacing the backbone. | Methods `subsec:baseline_interface`, Figure `fig:architecture`, Algorithm `alg:mgfrofr`. | Preserved |
| MGFE inserts learnable restoration tokens and forms coarse-to-fine branches. | Methods `subsec:mgfe`, Figure `fig:mgfe_detail`, equations around token insertion/fusion. | Preserved |
| MGFE uses channel-wise recalibration with scale/shift vectors. | Equations `eq:recalibration_context` and `eq:recalibration`. | Preserved |
| RATR is applied only during training and not during inference. | Methods `subsec:ratr`, Figure `fig:ratr_detail`, Algorithm `alg:mgfrofr`. | Preserved |
| RATR penalizes correlated temporal-similarity rankings across branches. | Equations `eq:dktau`, `eq:loss_intra`, and `eq:loss_ratr`. | Preserved |
| Training uses REDS and the synthetic degradation pipeline from MambaOFR. | Results `subsec:datasets` and `subsubsec:training_details`. | Preserved |
| Synthetic SRWOV has 30 held-out clips with paired ground truth. | Results `subsec:datasets`. | Preserved |
| Real-world SRWOV uses 216 clips and 29,256 frames without ground truth. | Results `subsec:datasets` and Table `tab:realworld` note. | Preserved |
| MgfrOFR achieves best PSNR/SSIM/LPIPS/DISTS in the synthetic comparison. | Table `tab:sota`. | Preserved |
| MgfrOFR improves PSNR by +1.14 dB over MambaOFR. | Table `tab:sota`, Results text, Conclusion. | Preserved |
| Wilcoxon tests show significant PSNR and SSIM differences. | Table `tab:sota` footnote and Results text. | Wording tightened |
| LPIPS and DISTS differences do not reach significance at N=30. | Table `tab:sota` footnote and Results text. | Preserved |
| MgfrOFR achieves best NIQE and BRISQUE on real-world SRWOV. | Table `tab:realworld`. | Preserved |
| MgfrOFR ranks second on CLIP-IQA+ behind OldPhoto. | Table `tab:realworld` and Discussion `subsec:failure`. | Preserved |
| Real-world no-reference gains should not be treated as ground-truth fidelity proof. | Results and Discussion limitations. | Wording tightened |
| Qualitative synthetic comparisons support local artifact suppression and structure preservation. | Figure `fig:qualitative_synthetic`. | Wording tightened |
| Qualitative real-world comparisons support artifact suppression and naturalness in selected examples. | Figure `fig:qualitative_realworld`. | Wording tightened |
| MGFE-only improves PSNR but degrades perceptual metrics. | Table `tab:ablation`. | Preserved |
| RATR-only improves PSNR more than MGFE-only under the ablation protocol. | Table `tab:ablation`. | Preserved |
| Full MgfrOFR is strongest across the ablation metrics. | Table `tab:ablation`. | Preserved |
| Sensitivity trends peak at the default configuration within the tested range. | Tables `tab:sensitivity_tau`, `tab:sensitivity_loss`, `tab:sensitivity_granularity`, Figure `fig:sensitivity`. | Wording tightened |
| MgfrOFR adds 0.011M parameters and 14.1G FLOPs over MambaOFR. | Table `tab:complexity`. | Preserved |
| RATR adds training-time cost but no additional inference parameters. | Methods, Results `subsec:complexity`, Discussion limitations. | Preserved |
| Branch similarity decreases from 0.42--0.66 to 0.11--0.37. | Figure `fig:branch_similarity`. | Preserved |
| Error maps show broader restoration gains rather than isolated fixes. | Figure `fig:branch_error_map`. | Wording tightened |
| MgfrOFR may struggle on single-degradation clips, extreme texture degradation, or severe motion blur. | Discussion `subsec:failure`. | Wording tightened |
| The main threats are dataset, metric, human-evaluation, baseline, and synthetic-to-real threats. | Discussion `subsec:limitations`. | Wording tightened |
| Funding, data availability, acknowledgments, conflicts, abbreviations, and author metadata. | `MGFROFR.tex` and `sections/authors.tex`. | Not edited |

## LaTeX Safety Checks

- **Compilation check:** Manual compilation was executed because the system `bibtex` symlink is broken. The successful sequence was `pdflatex`, `/usr/bin/bibtex.original`, `pdflatex`, `pdflatex`, `pdflatex`. The final log showed no undefined references or citations. The generated preview PDF was not included in the deliverable zip.
- **Static label/reference audit:** Labels remained 58/58; `\ref`/`\eqref` targets remained 49/49; citation keys remained 101/101; figure paths remained 9/9; `\input` paths remained 8/8.
- **Equation audit:** All equation environments and equation labels were preserved; normalized equation contents were unchanged.
- **Numerical audit:** Numerical tokens in edited `.tex` files were preserved, including all table values, p-values, percentages, FLOPs, parameters, memory, speed, PSNR, SSIM, LPIPS, DISTS, NIQE, BRISQUE, and CLIP-IQA+ values.
- **Figure audit:** All figure paths were preserved, including `figures/Fig7_sensitivity_analysis.png`. No `Fig8_convergence.pdf` path and no `fig:convergence` label were introduced.
- **Phrase audit:** The revised files do not contain the prohibited phrases: "to the best of our knowledge", "we observe that", "the key insight is", or "this result deserves careful interpretation".
- **Package audit:** Generated compiler byproducts were excluded from the final source zip.

## Unchanged Items

- No experimental numbers were changed.
- No citations or bibliography keys were changed.
- No labels, equation labels, or figure labels were changed.
- No equations or algorithm logic were changed.
- No table values or metric values were changed.
- No figure paths were changed.
- `Fig7_sensitivity_analysis.png` and `fig:sensitivity` were retained.
- No convergence/training-dynamics figure or section was reintroduced.
- `MGFROFR.tex`, `sections/authors.tex`, `references.bib`, `Definitions/`, and `figures/` were preserved except for the addition of this record and the diff file to the package.

## Remaining Risks

- The uploaded package begins `sections/discussion.tex` with `\subsection{Analysis and Limitations}` rather than a new `\section{Discussion}`. This structure was preserved to respect the instruction to preserve LaTeX structure and labels, even though a separate numbered Discussion section may be preferable editorially.
- The real-world evaluation still relies on no-reference metrics and qualitative inspection because no ground truth or human study is available.
- The baseline adaptation protocol remains a unified reproduction study rather than exhaustive re-optimization of all baselines.
- Compilation was verified in the available TeX environment using the MDPI class in the package. MDPI's production environment may make different float-placement decisions, but labels, references, citations, and figure paths are valid.
