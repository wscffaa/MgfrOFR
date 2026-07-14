# 03 Revision Round 2 Rework

Purpose: isolated second-round Symmetry revision package for the Fig.4/Fig.5 ROI-clarity issue.

Source of truth:
- `source/` contains the editable LaTeX source that previously lived at `projects/001-reidmamba/Paper/symmetry/`.
- `upload/` contains the clean manuscript, round1-to-round2 highlighted manuscript, source zip, cover letter, Supplementary Video S1, and the round2 Reviewer 2 response.
- `evidence/` contains validation logs, flattened round1/round2 TeX inputs for `latexdiff`, and the markdown source for the round2 response.
- `build/` stores generated PDF/log/cache artifacts.

Diff baseline:
- The highlighted-changes PDF is generated against `../02_revision_round1_rework/source/MGFROFR.tex`; it is a round1-revision to round2-revision diff, not an initial-submission to round2 diff.
