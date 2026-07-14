# Final Proof Verification Log

## Verdict

`CONDITIONAL-GO`: all author-side content, number, build, package, visual, attachment, public-repository, and SuSy upload gates pass. Publication placeholders and the final author confirmations remain external/human gates.

## 1. Query and author-metadata gate -- PASS

- `23` production `%MDPI` queries are retained.
- `23` following `%Author:` replies are present before the next query; orphan count is `0`.
- Every query is resolved by a corresponding correction or explicit confirmation in `proof-query-ledger.md`.
- Qi Zhang uses the project-007-verified ORCID `0009-0008-9432-7018`; the rejected old value is not active metadata.
- All original `53 \hl{}` markers are retained; the final source contains `3 \highlighting{}` markers.
- Q04 now expands REalistic and Dynamic Scenes (REDS) and region of interest (ROI) at first use in the main text and first affected caption; Q11 has no residual narrative italics.
- PDF text extraction contains no `%MDPI`, `%Author`, or general-note leakage.

## 2. Scientific-number gate -- PASS

- Current proof TeX SHA-256: `d5e685c98c61a7432615d415ee8b55e9cbfb531fc575e5877f6ad16386be1d8b`.
- Stage 1, production to the pre-closure answered proof, remains `PASS` under the existing literal and rendered-number reports.
- Stage 2, pre-closure proof to final proof, has exactly one authorized change: removal of the unsupported `7.6%` training-time value. The remaining `953` numeric tokens match in exact order; no number was added.
- The cross-method complexity table and paired configuration-level sanity benchmark are explicitly identified as distinct protocol-aligned snapshots; all complexity values are unchanged.
- Evidence: `final-number-gate-report.json` and the two stage-1 delta reports, followed by `final-number-authorized-delta-report.json` for the final source.

## 3. Build and package gate -- PASS

- Clean source build command: `latexmk -pdf -interaction=nonstopmode -halt-on-error symmetry-4339980-english.tex`.
- Final PDF: 28 A4 pages, 27 equations, 9 equation labels, 8 figures, and 5 tables.
- Final log scan contains no LaTeX Error, Fatal error, undefined control sequence, undefined citation/reference, or unresolved-rerun warning.
- `manuscript.zip` contains the TeX source, `references.bib`, `Definitions/`, and `figures/`; it contains no AUX, LOG, OUT, SyncTeX, FLS, FDB, or top-level manuscript PDF.
- `unzip -t manuscript.zip` passes.
- A fresh extraction of `manuscript.zip` compiles successfully. `submission_ready/manuscript.pdf` is the PDF from that independent build.
- Same-renderer comparison of the source-build and extracted-ZIP PDFs has `0/28` pixel mismatches; extracted PDF text is byte-identical.

## 4. Visual gate -- PASS

- All 28 pages were independently rendered and inspected; all figures, tables, equations, declarations, and references have no clipping, overlap, blank page, garbling, or unreadable label.
- Controlled floating keeps Figure 1 after the complete contribution list and keeps Algorithm 1 on a filled page. The maximum non-exempt continuous blank band is `24.8%`; page 25's `34.0%` back-matter transition is exempt because the following Abbreviations block is indivisible.
- Figure and table numbering and visual order remain monotonic. Figure 3's corrected notation and Figure 4/5 ROI labels remain legible.
- The placeholder editor, date, volume/issue/article number, and DOI remain a production-side HOLD and are covered by the non-rendering `%Author general note:`; MDPI internal commands were not edited.
- Evidence: `rendered-pages-second-stage-final-pass-20260711/page-01.png` through `page-28.png` and the independent final PDF audit.

## 5. Attachment gate -- PASS

- The MP4 remains byte-identical to the original download: SHA-256 `43efb7c7a88fdaf12e3d8bf3b1a12e2a2bae38195ac556082d5dc6fc98e56130`.
- Video probe: H.264, yuv420p, `1934 x 444`, 12 fps, 37.416667 s, 20,655,713 bytes.
- First, middle, and last frames were decoded and visually inspected in `video-frames/`.
- Non-published material and cover letter are byte-identical to their original/Round 2 counterparts.
- The Supplementary web slot rejects `.mp4`; the uploaded zero-compression ZIP contains only the unchanged MP4, and `unzip -t` plus inner-file SHA verification pass.

## 6. Repository-publicity gate -- PASS

- Local `gh` changed `wscffaa/MgfrOFR` from `PRIVATE` to `PUBLIC` with the explicit visibility-change acknowledgement.
- `gh repo view` reports `visibility=PUBLIC` and `isPrivate=false`.
- Anonymous HTTP returns `200`; credential-free `git ls-remote` resolves `HEAD` to `d4a1adab6c4cda38962a826e357cdc5497eaf71c`.
- The public root contains code, `options/`, `scripts/`, `tests/`, packaging metadata, a license, and citation metadata, so the Data Availability statement is externally true.

## 7. Historical SuSy web gate snapshot -- PASS; superseded by Section 9

- Live state: `Author proofreading`, manuscript `symmetry-4339980`, accepted `09 July 2026`.
- The replacement Manuscript ZIP (`13,436,039` bytes) and PDF (`13,395,167` bytes) were each triggered exactly once and reached `percent=100`, `uploading=false`, and `error=false`.
- All five staged files report strict `100%`; the two intentionally empty slots remain empty.
- Public e-mail settings remain Feifan Cai and Youdong Ding enabled, with Qi Zhang, Kun Yang, and Lei Chen disabled. Publication-notification e-mail remains blank.
- All four confirmation checkboxes and both confirmation-name fields remain empty/unchecked.
- Neither `Confirm and Continue` nor final `Submit` was clicked.
- Evidence: `web-upload-readback.md` and `raw/susy-author-proofreading-after-closure.png`.

## 8. Historical explicit five-slot re-upload -- PASS; superseded by Section 9

- At the author's request, all five populated Step 2 slots were re-uploaded sequentially from `submission_ready/`.
- The final browser readback matches the five local filenames and exact byte counts; every populated slot reports `100%`, `uploading=false`, `error=false`, and a new SuSy `hashKey`.
- Figures/Graphics and Graphical Abstract remain empty.
- The page remains at `Author proofreading`; the final `Submit` button was not clicked.
- This pass targeted only file inputs. At the final readback, all five public-email boxes and all four proof-confirmation boxes were already checked and both confirmation-name fields contained `feifan cai`; these controls were not changed.
- Evidence: the second section of `web-upload-readback.md` and the two targeted `raw/susy-step2-*-after-reupload-20260710.png` screenshots.

## 9. English-editor instruction and final Step 2 upload -- PASS; supersedes earlier live readbacks

- Compared the final proof against the frozen production baseline: `953/953` numeric tokens remain in exact order; all 27 equation bodies are byte-exact; 8 figures, 5 tables, labels, image paths, and 101 citation keys retain order and content.
- The abstract, main text, and first affected figure/table were audited as independent acronym scopes. All three pass; Q04 records the full closure.
- The contribution-summary wording retains the relative claim `at modest additional computational cost`; the rejected absolute claim does not appear.
- Final `manuscript.zip` is 13,438,207 bytes with SHA-256 `4152460d8e7252c4324582b5b03b3c30efc7015a0ce4029c09d939f64ac85696`.
- Final independently rebuilt `manuscript.pdf` is 13,397,653 bytes with SHA-256 `7f33ec06185060db77868514a47d8b279ce10f4679173ddb09ba37afc5ec9c4c`.
- All five populated Step 2 slots match their local filenames and exact byte sizes; all derive `100%`, have `uploading=false`, `error=false`, and a non-empty SuSy `hashKey`. The two optional image slots remain empty.
- The three final proof checkboxes remain unchecked, the confirmation-name and publication-notification e-mail fields remain blank, and final `Submit` was not clicked. Step 1 was not edited.
- Evidence: `english-editor-change-and-abbreviation-audit.md`, `second-stage-number-structure-report.json`, the final section of `web-upload-readback.md`, and the two `raw/susy-step2-*-final-20260711.png` screenshots.

## 10. Proof Cover Letter correction -- PASS; final Submit pending

- The former `coverletter.v3.pdf` was confirmed to be a Round 2 letter and is superseded.
- `coverletter-final-proof.pdf` is one A4 page, 95,399 bytes, SHA-256 `f3ba6c13627d5088ad76741195fdf349029e7eb0e060d17526360afd13a7341f`.
- Extracted text contains `Author Proofreading / Final Proof`, `23 copy-editor queries`, and `28-page`; it contains no `Second revised manuscript`, `Reviewer 2`, or `Round-2` text.
- Visual rendering passes with no clipping, overlap, broken glyph, or overflow.
- The live Cover Letter slot matches the new filename and exact byte size at derived `100%`, `uploading=false`, `error=false`, with SuSy `hashKey=be237201d38f44f493d2e1f0c740f764`.
- All other upload-slot `hashKey` values remain unchanged. The existing proof confirmations/signature were not modified and final `Submit` was not clicked.
