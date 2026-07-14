# Submission Checklist

## Upload Set

| Slot | File | Status |
|---|---|---|
| Manuscript PDF | `upload/MGFROFR-clean.pdf` | OK |
| Highlighted changes | `upload/MGFROFR-highlighted-changes.pdf` | OK |
| LaTeX source | `upload/MGFROFR-latex-source.zip` | OK |
| Response to Reviewer 1 | `upload/Response-to-reviewer1-round1.docx` | OK |
| Response to Reviewer 2 | `upload/Response-to-reviewer2-round1.docx` | OK |
| Cover letter | `upload/Cover-Letter.pdf` | OK |
| Supplementary video | `upload/Supplementary_Video_S1.mp4` | OK, H.264/yuv420p MP4 (20,655,713 bytes, two-part: synthetic PSNR + real-world NR), declared in `\supplementary{}` and both response letters |

## Validation Evidence

| Check | Evidence |
|---|---|
| Clean manuscript build | `latexmk -pdf -interaction=nonstopmode -halt-on-error MGFROFR.tex`; PDF has 27 pages |
| Clean manuscript log gate | `rg "LaTeX Error|Fatal error|undefined|Citation|There were undefined|not found|No file|Rerun to get" MGFROFR.log` returned no matches after final build |
| Source zip compile | extracted `MGFROFR-latex-source.zip` to a clean temp dir and rebuilt with `latexmk`; PDF has 27 pages |
| Highlighted changes compile | rebuilt `MGFROFR-diff.tex` from byte-reproducible `latexpand --empty-comments` flats using red-delete/blue-add `latexdiff --config='PICTUREENV=(?:figure\|table\|table\\*\|sidewaystable\|algorithm\|algorithmic\|tabular\|tabularx)[\\w\\d*@]*' --graphics-markup=none`; `--no-del` is absent; PDF has 32 pages; final log gate returned no matches |
| Response DOCX schema | `officecli validate` passed for both response files |
| Source zip manifest | `source-zip-manifest.txt` excludes old `Fig9c`, `Fig10`, `Fig7`, and supplementary video files |
| Internal-variant text gate | active LaTeX source, flattened source, highlighted diff source, highlighted PDF text extracted with `pypdf`, source zip contents, and response DOCX raw XML returned no public internal-variant-label matches |
| Clean manuscript process-language gate | `PASS clean-source internal/revision language scan` after removing `project-internal`, `frozen`, `submitted model`, `current 001`, `007`, and response-process wording from the clean manuscript source |
| Cover letter stale-claim gate | `PASS cover-letter stale-claim scan` after regenerating `Cover-Letter.pdf`; stale claims about branch activation/response maps, training-time branch-similarity curves, three-class ROI annotations, expert subjective evaluation, and F1/D1/internal freeze wording are absent |
| Visual spot check | Rendered PDF pages 16--18; Figure 4 now shares page 16 with the Ablation Study opener and Table 3, Figure 5 remains readable on page 17, and Figure 6/Table 4 fit on page 18 |
| R2-C5 reproducibility consistency | Token initialization is now stated in Method (`standard deviation 0.02`), Cover Letter, and Reviewer 2 response; no Appendix claim is made |
| GenAI language-polishing disclosure | `Acknowledgments` now disclose OpenAI Codex (GPT-5, accessed 1 July 2026) solely for language polishing; no Methods statement was added because no AI-assisted study design, data, graphics, experiments, analysis, or interpretation is declared |

## Known Advisory

`officecli view ... issues` reports generic first-line-indent format suggestions for the response letters. The DOCX schema validation passes, and the response files retain block-style reviewer-response formatting.

The current final-candidate upload set totals 103,394,411 bytes (103.394 MB / 98.605 MiB), below the Symmetry 120 MB total-file limit. The reduction comes from recompressing the largest qualitative figure and rebuilding the clean PDF, highlighted PDF, and LaTeX source zip from that asset.
