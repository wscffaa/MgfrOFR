# Submission Checklist

## Upload Set

| Slot | File | Status |
|---|---|---|
| Manuscript PDF | `upload/MGFROFR-clean.pdf` | OK |
| Highlighted changes | `upload/MGFROFR-highlighted-changes.pdf` | OK |
| LaTeX source | `upload/MGFROFR-latex-source.zip` | OK |
| Response to Reviewer 2 Round 2 | `upload/Response-to-reviewer2-round2.docx` | OK, regenerated in the round1 reviewer-response format on 2026-07-08 |
| Cover letter | `upload/Cover-Letter.pdf` | OK, regenerated for the second revised manuscript on 2026-07-08 |
| Supplementary video | `upload/Supplementary_Video_S1.mp4` | OK, H.264/yuv420p MP4 (20,655,713 bytes, two-part: synthetic PSNR + real-world NR), declared in `\supplementary{}` |

## Validation Evidence

| Check | Evidence |
|---|---|
| Final GPTPro MDPI/CV polish gate | `gptpro-final-mdpi-cv-polish-20260708/number_gate_report.json` reports verdict `PASS`, 272 frozen literals, and 0 failures |
| Clean manuscript build | after final GPTPro merge, `latexmk -pdf -interaction=nonstopmode -halt-on-error MGFROFR.tex`; PDF has 27 pages |
| Clean/highlighted log gate | `rg "LaTeX Error|Fatal error|undefined|Citation|There were undefined|not found|No file|Rerun to get|Warning--" MGFROFR.log MGFROFR-highlighted-changes.log` returned no matches after final build |
| Source zip compile | after final GPTPro merge, extracted `MGFROFR-latex-source.zip` to a clean temp dir and rebuilt with `latexmk`; PDF has 27 pages |
| Highlighted changes compile | after final GPTPro merge, rebuilt round1-to-round2 highlighted changes with `latexpand` and `latexdiff --graphics-markup=none`; PDF has 27 pages |
| Reference/citation gate | after final GPTPro merge, local citation scan reports 48 cited keys, 48 BibTeX entries, 0 missing keys, and 0 unused entries |
| Response DOCX schema and format | `officecli validate` passed for the regenerated `Response-to-reviewer2-round2.docx`; `officecli view ... annotated` confirms the round1-style title, Summary, Questions for General Evaluation table, and point-by-point `Comments/Response/Revision made/Evidence location` structure; `unzip -p ... word/document.xml` confirms the same content is physically saved to disk; page-1 screenshot is saved at `evidence/docx-format-check/Response-to-reviewer2-round2-page1.png` |
| Cover letter round-2 check | regenerated from `evidence/Cover_Letter_MgfrOFR_Symmetry_round2.tex`; PDF text begins with `July 8, 2026` and contains no `Major Revision`, `July 1`, `Reviewer 1`, or `two reviewers` residue |
| Source zip manifest | `source-zip-manifest.txt` includes the cropped Fig.1 PDF, cropped Fig.2 PDF, and the revised Fig.4/Fig.5 PDF assets |
| Fig.1 crop check | extracted source zip Fig.1 is `910 x 406 pt` after `pdfcrop` from `Paper/assets/figure-sources/Pipline.pdf` |
| Fig.2 crop check | `figures/Fig2_mgfe_module_detail.pdf` was cropped from `959.76 x 540 pt` to `914 x 401 pt`; rendered page 7 is saved as `evidence/fig2-replacement/clean-page07-fig2-07.png` |
| Visual/page audit | after final GPTPro merge, rendered clean pages 15--18 to `rendered-page-checks-final-gptpro/` and scanned all 27 clean pages plus all 27 highlighted-change pages; blank-space audit reports `bad_count=0`; Figure 4 and Figure 5 remain readable on pages 16--17 with no right-edge clipping |
| Live SuSy reviewer check | `susy-reviewer2-round2-web-check.md` records the Reviewer 2 Round 2 live-page issues and confirms no SuSy reply was submitted during the check |
| Response alignment | SuSy Reviewer 2 Round 2 comments were checked on the live page; `response-to-reviewer2-round2.md` now answers the RATR complementarity, LPIPS/DISTS ablation, Fig.4/Fig.5 ROI, and proofreading comments and matches the upload DOCX |
| Upload inventory | `upload-file-sizes.txt` and `upload-sha256.txt` refreshed after regenerating the clean PDF, highlighted PDF, source zip, and response DOCX |

## Known Advisory

`officecli view ... issues` may report generic first-line-indent format suggestions for the response letter. The DOCX schema validation passes, and the response file retains block-style reviewer-response formatting.

The current final-candidate upload set totals 60,772,429 bytes (60.772 MB / 57.957 MiB), below the Symmetry 120 MB total-file limit.
