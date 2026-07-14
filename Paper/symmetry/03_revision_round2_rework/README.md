# 001 ReidMamba / MgfrOFR Symmetry Revision Round 2 Rework

This directory is the isolated second-round upload candidate for the Fig.4/Fig.5 ROI-clarity revision. The editable source lives under `source/`; generated build artifacts are under `build/`.

Upload files are under `upload/`:

- `MGFROFR-clean.pdf`
- `MGFROFR-highlighted-changes.pdf` generated from round1 revision to round2 revision
- `MGFROFR-latex-source.zip`
- `Response-to-reviewer2-round2.docx`
- `Cover-Letter.pdf`
- `Supplementary_Video_S1.mp4`

Do not upload round1 response letters from this round2 directory. Supplementary Video S1 remains included as a standalone supplementary file (H.264/yuv420p MP4, 20,655,713 bytes, two parts: REDS-synthetic with GT and per-frame PSNR, then real-world SRWOV with overall NIQE/BRISQUE), and the manuscript still declares it through the `\supplementary{}` statement.

The copied round1 response DOCX files are archived under `evidence/round1-response-archive/` for traceability only.

Validation evidence is under `evidence/`:

- `clean-final-latex.log`
- `source-zip-final-latex.log`
- `MGFROFR-round1-flat.tex`
- `MGFROFR-round2-flat.tex`
- `response-to-reviewer2-round2.md`
- `source-zip-manifest.txt`
- `upload-file-sizes.txt`
- `upload-sha256.txt`

Key checks completed:

- Clean manuscript builds to 27 pages.
- Source zip independently builds to 27 pages.
- Highlighted changes PDF builds to 27 pages from `../02_revision_round1_rework/source/` to this round2 source tree.
- Source zip manifest excludes `Fig9c_branch_sim_evolution.pdf`, `Fig10_failure_cases.pdf`, `Fig7_sensitivity_analysis.png`, and supplementary video files; Supplementary Video S1 is uploaded separately as a standalone supplementary file (H.264 MP4, yuv420p, 20,655,713 bytes, 37.4 s; part 1 REDS-synthetic with GT and per-frame PSNR, part 2 real-world SRWOV with overall NIQE/BRISQUE).
- Supplementary Video S1 is referenced in the manuscript (`results.tex`) and declared in `\supplementary{}`.
- The round2 response DOCX validates with `officecli validate`.
- Active manuscript, highlighted diff, source zip, and response DOCX text surfaces have no public internal-variant-label matches; internal variant labels remain only in experiment ledgers outside the upload package.
