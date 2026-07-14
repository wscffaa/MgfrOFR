# 001 ReidMamba / MgfrOFR Symmetry Revision Round 1 Rework

This directory is the reworked upload candidate after restoring the experiment figures to the full-method qualitative comparison style. The editable source now lives under `source/`; generated build artifacts are under `build/`.

Upload files are under `upload/`:

- `MGFROFR-clean.pdf`
- `MGFROFR-highlighted-changes.pdf`
- `MGFROFR-latex-source.zip`
- `Response-to-reviewer1-round1.docx`
- `Response-to-reviewer2-round1.docx`
- `Cover-Letter.pdf`
- `Supplementary_Video_S1.mp4`

Do not upload the old `revision_round1/upload/MGFROFR-supplementary-files.zip` for this reworked package. Supplementary Video S1 is included as a standalone supplementary file (H.264/yuv420p MP4, 20,655,713 bytes, two parts: REDS-synthetic with GT and per-frame PSNR, then real-world SRWOV with overall NIQE/BRISQUE), and the manuscript now declares it through the `\supplementary{}` statement.

Validation evidence is under `evidence/`:

- `clean-final-latex.log`
- `source-zip-final-latex.log`
- `diff-final-latex.log`
- `MGFROFR-old-first-submission-flat.tex`
- `source-zip-manifest.txt`
- `upload-file-sizes.txt`
- `upload-sha256.txt`

Key checks completed:

- Clean manuscript builds to 27 pages.
- Source zip independently builds to 27 pages.
- Highlighted changes PDF builds to 32 pages against `../01_initial_submission/source/`, extracted from the SuSy initial-submission package preserved in `../01_initial_submission/upload/manuscript.zip`.
- Source zip manifest excludes `Fig9c_branch_sim_evolution.pdf`, `Fig10_failure_cases.pdf`, `Fig7_sensitivity_analysis.png`, and supplementary video files; Supplementary Video S1 is uploaded separately as a standalone supplementary file (H.264 MP4, yuv420p, 20,655,713 bytes, 37.4 s; part 1 REDS-synthetic with GT and per-frame PSNR, part 2 real-world SRWOV with overall NIQE/BRISQUE).
- Supplementary Video S1 is referenced in the manuscript (`results.tex`) and declared in `\supplementary{}`; both response letters state the video is now provided.
- Response DOCX files validate with `officecli validate`.
- Active manuscript, highlighted diff, source zip, and response DOCX text surfaces have no public internal-variant-label matches; internal variant labels remain only in experiment ledgers outside the upload package.
