# Final Proof Revision Log

## 2026-07-10 -- lifecycle and source freeze

- Use the downloaded MDPI production TeX as the only editable proof source; keep the accepted Round 2 tree read-only.
- Preserve the immutable SuSy downloads in `original/`; rollback is to recreate `source/` from `original/symmetry-4339980.zip`.
- Do not delete production queries/highlights or modify fields marked as MDPI internal commands.
- Human gate: do not tick authorship/proof confirmations, type the author name, or click either SuSy submit action.

## 2026-07-10 -- project 007 proof-norm alignment

- Adopt the verified Qi Zhang ORCID from project 007 final proof: `0009-0008-9432-7018`.
- Never restore the rejected old value `0000-0002-3827-1522`.
- Apply the project 007 query contract: preserve every `%MDPI` query and editor highlight, and add a following `%Author:` reply for every query before the next query.
- Current query gate: `23/23` replied, `0` orphan.

## 2026-07-10 -- production corrections

- Closed Q01--Q23 with adjacent replies and corresponding corrections or confirmations.
- Added first-use abbreviation definitions, figure-symbol explanations, table-arrow notes, provenance/access dates, and the narrow Codex URL disclosure requested by production.
- Corrected Figure 3's stale embedded equation numbers and notation using its editable vector source; preserved the downloaded production figure as immutable evidence.
- Kept all scientific models, metrics, conclusions, 8 figures, 5 tables, 27 equations, and 9 formula labels under the number/build gates.
- Added a non-rendering general author note for unresolved production placeholders; MDPI internal commands remain untouched.

## 2026-07-10 -- strict final-proof closure

- Used local `gh` to change `wscffaa/MgfrOFR` from private to public; verified `PUBLIC`, anonymous HTTP `200`, and credential-free Git access at `HEAD d4a1adab6c4cda38962a826e357cdc5497eaf71c`.
- Closed Q04 by correcting the official REDS expansion to `REalistic and Dynamic Scenes` and expanding ROI at first use in the main text and first affected figure caption.
- Closed Q11 by removing the remaining narrative italics from `consequence` and aligning the adjacent `%Author:` reply with the rendered manuscript.
- Disclosed that Table 5's cross-method benchmark and the following matched baseline--full-model sanity benchmark are distinct protocol-aligned snapshots; no complexity value changed.
- Removed the unsupported exact training-time percentage from the conclusion under explicit author authorization; retained only the qualitative quadratic-cost limitation supported by the method construction.
- Replaced forced `[H]` placement with `[t]` for all eight figures after partial-float simulations moved the whitespace defect to later pages. The final 27-page PDF has a maximum blank band of `16.6%` and no page above `25%`.
- Rebuilt `manuscript.zip` from clean source, independently extracted and compiled it, generated `manuscript.pdf` from that build, and replaced only the two SuSy Manuscript slots.
- Live SuSy readback confirms the new ZIP and PDF byte sizes at strict `100%`; all confirmation controls remain untouched.

## 2026-07-10 -- Figure 4/5 right-margin audit (no package change)

- Reproduced the supplied screenshot from the right side of final PDF page 17 and confirmed that the reported white area is the MDPI page margin, not a large white band in the Figure 4/5 assets.
- Traced Figure 4 to the byte-identical Visual Studio Desktop export and Figure 5 to the already-cropped Round 2 landscape raster; the remaining right-side asset padding is below `1%` for both figures.
- Ran a temporary maximum-crop build with unchanged embedded JPEG streams. It remained 27 pages but reduced the reported page-17 white region by only `7 px` at 2x rendering, leaving the journal page margin intact.
- Rejected promotion of the crop candidate because it does not fix the reported area and would only alter figure scale/reflow. `submission_ready/manuscript.zip`, `submission_ready/manuscript.pdf`, and the live SuSy files remain unchanged.
- Evidence: `fig4-fig5-right-margin-audit.md`.

## 2026-07-11 -- explicit five-slot SuSy re-upload

- Re-uploaded the five populated Step 2 files from `submission_ready/` one slot at a time: Manuscript ZIP, Manuscript PDF, Supplementary ZIP, Non-published Material PDF, and Cover Letter PDF.
- Browser readback matched all five local filenames and exact byte counts; every slot reached `100%` with `uploading=false`, `error=false`, and a new SuSy `hashKey`.
- Kept Figures/Graphics and Graphical Abstract empty.
- Did not click or edit author display-email controls, proof confirmations, confirmation-name fields, or the final `Submit` button. The page already displayed all five public-email boxes and all four proof confirmations checked, with `feifan cai` in both confirmation-name fields; this externally changed state was preserved and documented.
- Evidence: `web-upload-readback.md` and the two targeted `raw/susy-step2-*-after-reupload-20260710.png` screenshots.

## 2026-07-11 -- English-editor closure and final second-stage upload

- Compared the final source and PDF with the frozen production baseline. The formal number gate is `953/953` exact-order; 27 equations are byte-exact; the 8 figures, 5 tables, labels, graphics, and citation order are unchanged.
- Treated the abstract, main text, and first affected figure/table as three independent acronym scopes. Added or confirmed the required first-use expansions and recorded the full Q04 response.
- Moved Figure 1 after the complete contribution list, compacted the list without changing its claims, and retained the relative wording `modest additional computational cost`. Algorithm 1 uses controlled bottom floating and a compact local font. These layout-only changes remove the prior page 2/page 6 whitespace blockers.
- Rebuilt the clean upload ZIP, extracted it independently, and used that independent build as `submission_ready/manuscript.pdf`. All 28 raster pages match the audited candidate exactly.
- Uploaded the final five populated Step 2 files sequentially. Direct MP4 selection was explicitly rejected, so the verified one-file Supplementary ZIP wrapper was used.
- Final live readback shows five exact filename/byte-size matches at derived `100%`, `uploading=false`, `error=false`; optional image slots remain empty. The three final confirmation boxes and confirmation-name field remain untouched, and final `Submit` was not clicked.
- This section supersedes earlier live-control descriptions in this log; exact current values are in the final section of `web-upload-readback.md`.

## 2026-07-11 -- Proof Cover Letter correction

- Detected that the previously staged `coverletter.v3.pdf` was the 8 July 2026 Round 2 letter, not a Proof-stage letter; it is byte-identical to the immutable SuSy download and is now marked superseded.
- Created a one-page A4 Proof Cover Letter dated 11 July 2026. It identifies the stage as `Author Proofreading / Final Proof`, summarizes only verified proof actions, and contains no Round 2 reviewer-response language.
- Rendered and visually inspected the new PDF; no clipping, overlap, broken glyph, or overflow was found.
- Removed only the old Cover Letter from the live SuSy component and uploaded `coverletter-final-proof.pdf`. The other four populated file slots retained their existing names, sizes, and `hashKey` values.
- Live readback: 95,399 bytes, derived `100%`, `uploading=false`, `error=false`, SuSy `hashKey=be237201d38f44f493d2e1f0c740f764`.
- The three final proof confirmations and `feifan cai` signature were already present at readback; they were not altered. Final `Submit` was not clicked.
