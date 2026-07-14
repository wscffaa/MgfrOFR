# Submission Checklist - MgfrOFR Round 1 Major Revision

> **Status**: Local final package candidate. Built and verified on 2026-06-30.
> **Journal**: Symmetry (MDPI) · **Manuscript ID**: symmetry-4339980
> **Date**: 2026-06-30

---

## 1. Identity and metadata

| Item | Value | Status |
|---|---|---|
| Manuscript ID | symmetry-4339980 | OK |
| Title | Multi-Granularity Feature Decomposition with Ranking-Aware Regularization for Old Film Restoration | OK |
| Journal / Special Issue | Symmetry - Symmetry in Artificial Intelligence and Applications | OK |
| Submission type | Resubmission after Major Revision | OK |
| Main model | F1 (MGFE+RATR, average fusion) | OK |

---

## 2. Upload file manifest

| File | Size | Evidence | Status |
|---|---:|---|---|
| `MGFROFR-clean.pdf` | 7,826,014 B | `pdfinfo`: 28 pages; `latexmk` clean build | OK |
| `MGFROFR-highlighted-changes.pdf` | 7,826,031 B | `pdfinfo`: 28 pages; final diff log has no unresolved refs/citations | OK |
| `Cover-Letter.pdf` | 145,763 B | `pdfinfo`: 2 pages | OK |
| `Response-to-reviewer1-round1.docx` | 41,363 B | `officecli validate`: no errors | OK |
| `Response-to-reviewer2-round1.docx` | 42,068 B | `officecli validate`: no errors | OK |
| `MGFROFR-supplementary-files.zip` | 7,072,635 B | contains `MGFROFR-supplementary.pdf` and `Supplementary_Video_S1.mp4` for the SuSy Supplementary File(s) slot | OK |
| `MGFROFR-latex-source.zip` | 14,853,245 B | 35 files; independent zip compile produced 28-page PDF | OK |

Upload files are stored under `revision_round1/upload/`.

## 2b. Evidence and preview files

| File | Size | Evidence | Status |
|---|---:|---|---|
| `previews/Response-to-reviewer1-round1.pdf` | 124,983 B | `pdfinfo`: 4 pages | OK |
| `previews/Response-to-reviewer2-round1.pdf` | 133,235 B | `pdfinfo`: 5 pages | OK |
| `supplementary-source/MGFROFR-supplementary.pdf` | 166,483 B | `pdfinfo`: 2 pages | OK |
| `supplementary-source/Supplementary_Video_S1.mp4` | 6,909,398 B | source file packaged into supplementary zip | OK |
| `supplementary-files-manifest.txt` | 373 B | generated from `upload/MGFROFR-supplementary-files.zip` | OK |
| `source-zip-manifest.txt` | 2,338 B | generated from `upload/MGFROFR-latex-source.zip` | OK |
| `diff-build.log` | 76,392 B | records highlighted-diff build | OK |
| `source-zip-compile.log` | 54,014 B | records independent source-zip compile | OK |
| `clean-final-latex.log` | 61,146 B | final clean-manuscript TeX log; error/reference scan has no hits | OK |
| `diff-final-latex.log` | 62,241 B | final highlighted-diff TeX log; error/reference scan has no hits | OK |
| `source-zip-final-latex.log` | 61,146 B | final source-zip TeX log; error/reference scan has no hits | OK |

---

## 3. Response-letter checks

| Check | Reviewer 1 slot | Reviewer 2 slot | Status |
|---|---|---|---|
| SuSy slot mapping | local R2 content | local R1 content | OK |
| Point-by-point blocks | 6 | 10 | OK |
| MDPI template sections | Summary / General Evaluation / Point-by-point / English / Additional | Summary / General Evaluation / Point-by-point / English / Additional | OK |
| Plain reviewer headings | `Comments N:` / `Response N:` / `Revision made:` | `Comments N:` / `Response N:` / `Revision made:` | OK |
| Internal marker scan | no hits in generated DOCX text | no hits in generated DOCX text | OK |
| Closing paragraph | present once at document end | present once at document end | OK |

---

## 4. PDF / LaTeX checks

| Check | Clean manuscript | Highlighted changes | Status |
|---|---|---|---|
| Build command completed | `latexmk -pdf -interaction=nonstopmode -halt-on-error MGFROFR.tex` | `pdflatex/bibtex/pdflatex/pdflatex` on `MGFROFR-diff.tex` | OK |
| Final log error scan | no LaTeX/file/control/fatal errors | no LaTeX/file/control/fatal errors | OK |
| Final reference scan | no unresolved refs/citations or rerun notice | no unresolved refs/citations or rerun notice | OK |
| Page count | 28 | 28 | OK |
| Source zip compile | 28 pages from temporary unzip directory | n/a | OK |

---

## 5. Supplementary material

| Item | Decision | Status |
|---|---|---|
| Protocol PDF | Retained as `MGFROFR-supplementary.pdf` | OK |
| Supplementary Video S1 | `Supplementary_Video_S1.mp4`, 6.9 MB, side-by-side temporal comparison | OK |
| SuSy supplementary upload bundle | `MGFROFR-supplementary-files.zip` contains the protocol PDF and Video S1 | OK |
| Manuscript supplementary statement | `MGFROFR.tex` now references Supplementary Video S1 | OK |

---

## 6. Upload notes for SuSy

- Upload `Response-to-reviewer1-round1.docx` to the SuSy Reviewer 1 response slot.
- Upload `Response-to-reviewer2-round1.docx` to the SuSy Reviewer 2 response slot.
- In each SuSy reply text box, enter: `Please see the attachment.`
- Main resubmit form slot map: `* Manuscript (Word/ZIP/RAR)` -> `MGFROFR-latex-source.zip`; `Manuscript (PDF Version)` -> `MGFROFR-clean.pdf`; `Supplementary File(s)` -> `MGFROFR-supplementary-files.zip`; `Non-published Material (Word/ZIP/PDF)` -> `MGFROFR-highlighted-changes.pdf`; `Cover Letter(PDF)` -> `Cover-Letter.pdf`.
- Leave `Figures, Graphics, Images` empty because final figure files are already included in the LaTeX source zip; leave `Graphical Abstract` empty because no graphical abstract is used.
- Select `No` for `Authorship Changed?`; if authorship changes, the page requires an Authorship Change Form, which is not part of this package.

---

## 7. Remaining human gate

- Online SuSy upload and final submit still require manual confirmation on the MDPI page.
- This checklist is evidence for local package readiness only; it does not mean the package has been uploaded.
