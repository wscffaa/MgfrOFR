# Final GPTPro MDPI/CV-Language Pass

You are acting as two roles at once:

1. a senior computer-vision paper editor aiming for concise top-tier CV conference English;
2. an MDPI/Symmetry reviewer checking whether the manuscript text clearly answers the Round-2 reviewer concerns.

Please edit the manuscript language only. Do not change the science, claims, experiments, numbers, formulas, figure/table numbering, citations, labels, file paths, or LaTeX structure.

## Input Files

- `files/evidence/gptpro-final-mdpi-cv-polish-20260708/01_manuscript_current_full.tex`
  - This is the full current manuscript text.
  - It contains `%% OFR_SEGMENT_BEGIN ...` and `%% OFR_SEGMENT_END ...` sentinels.
- `files/evidence/gptpro-final-mdpi-cv-polish-20260708/04_FROZEN_numbers.md`
  - Every listed numeric literal must remain unchanged.
- `files/evidence/gptpro-final-mdpi-cv-polish-20260708/02_reference_citation_report.md`
  - Citation/reference gate context.
- `files/evidence/response-to-reviewer2-round2.md`
  - Reviewer 2 Round-2 response context.
- `files/evidence/susy-reviewer2-round2-web-check.md`
  - Live-page reviewer issue context.
- `files/evidence/submission-checklist.md`
  - Current submission validation context.
- `files/source/references.bib`
  - Reference list context only.

## Reviewer-Facing Checks

While editing, verify that the manuscript text reads as if it has addressed these Round-2 concerns:

- RATR and MGFE complementarity is explained clearly and without overclaiming.
- LPIPS/DISTS ablation evidence is described with the right boundary: perceptual benefit, not blanket superiority.
- Fig.4 and Fig.5 ROI improvements are described clearly and consistently.
- Real-world Fig.5 is described without implying ground-truth availability.
- The prose is polished enough that a reviewer should not raise a remaining English-quality objection.
- The writing style is concise, technical, and natural for a strong computer-vision paper.

## Hard Constraints

- Preserve every `%% OFR_SEGMENT_BEGIN` and `%% OFR_SEGMENT_END` line exactly.
- Return all seven segments in the same order.
- Preserve every frozen number exactly.
- Preserve all `\label{...}`, `\ref{...}`, `\cref{...}`, `\cite{...}`, `\citep{...}`, `\citet{...}`, formulas, tables, figure paths, and includegraphics commands.
- Do not add new references.
- Do not remove references.
- Do not invent new results, datasets, reviewer claims, or statistical outcomes.
- Do not insert reviewer-response meta language into the manuscript, such as "the reviewer", "round", "revision", "response letter", or "we have addressed".
- Do not rewrite the response letter. Use it only to ensure that the manuscript wording is aligned with the response.

## Output Format

Return exactly one complete LaTeX code block containing the full edited manuscript from `%% OFR_SEGMENT_BEGIN abstract ...` through `%% OFR_SEGMENT_END conclusion`.

No explanations before or after the code block.
