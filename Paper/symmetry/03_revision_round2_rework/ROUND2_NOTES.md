# Round 2 Revision Notes

Date: 2026-07-08

Purpose:
- Isolate the second-round Fig.4/Fig.5 ROI-quality revision from `02_revision_round1_rework`.
- Use the new Desktop-exported PDF figures only in this round2 workspace.
- Treat `02_revision_round1_rework/source/MGFROFR.tex` as the old manuscript and this directory's `source/MGFROFR.tex` as the new manuscript for highlighted changes.

Figure replacements:
- Fig.1: `source/figures/Fig1_mgfrofr_architecture.pdf` was replaced from `Paper/assets/figure-sources/Pipline.pdf` and cropped with `pdfcrop`; the final cropped figure size is `910 x 406 pt`.
- Fig.2: `source/figures/Fig2_mgfe_module_detail.pdf` was replaced from `Paper/assets/figure-sources/Fig2.pdf` and cropped with `pdfcrop`; the final cropped figure size is `914 x 401 pt`.
- Fig.4: `source/figures/Fig4_SOTA_Synthetic_REDS_synthetic_Qualitative.pdf`
- Fig.5: `source/figures/Fig5_SOTA_RealWorld_RealFilm_SRWOV_Qualitative.pdf`
- Fig.5 was regenerated as a Fig.4-style landscape dense ROI matrix (`493.2 x 425.76 pt`) because the earlier portrait asset (`493.2 x 595.2 pt`) caused the rendered page to leave a large right-side blank area under height-constrained scaling.

Text synchronization:
- `source/sections/results.tex` now describes Fig.4 as full degraded input frames plus enlarged ROI crops.
- Fig.5 is described as three RealFilm-SRWOV real-world clips without GT, evaluated by artifact suppression, structural preservation, naturalness, and local texture.
- Fig.5 caption explicitly states that colored boxes mark selected ROI regions and enlarged crops compare local restoration details.
- Fig.4 uses fixed placement with a slightly larger height-constrained scale so the following Fig.5 discussion fills the previous blank area below the Fig.4 caption.
- Fig.5 now uses the same `width=1.33\textwidth,height=0.66\textheight,keepaspectratio` includegraphics parameters as Fig.4; the highlighted manuscript uses a compact manual deletion summary for the old clip-ID list to avoid a marked-only blank page.
- Fig.4 float placement was changed from forced `[H]` to top-preferred `[!t]` so LaTeX can move the large ROI matrix to the next page and fill the previous page with subsequent discussion text instead of leaving a large bottom blank area.

Reviewer response:
- `upload/Response-to-reviewer2-round2.docx` answers the second-round ROI-clarity concern for Fig.4/Fig.5.
- `evidence/response-to-reviewer2-round2.md` is the editable text source for that response.
- Copied round1 response DOCX files are archived under `evidence/round1-response-archive/` and are not round2 upload files.

Validation performed:
- Clean manuscript: `latexmk -g -pdf -interaction=nonstopmode -halt-on-error MGFROFR.tex`
- Highlighted changes: `latexpand` both round1 and round2 source trees, then `latexdiff` round1 flat source against round2 flat source, then `latexmk -g -pdf -interaction=nonstopmode -halt-on-error MGFROFR-highlighted-changes.tex`
- Source zip independent compile from `upload/MGFROFR-latex-source.zip`
- Source zip Fig.1 check: extracted `figures/Fig1_mgfrofr_architecture.pdf` remains `910 x 406 pt`.
- Source zip Fig.2 check: extracted `figures/Fig2_mgfe_module_detail.pdf` remains `914 x 401 pt`.
- Rendered clean PDF pages 16--18 to verify Fig.4/Fig.5 placement and caption fit.
- Rendered all 27 clean pages and all 27 highlighted-change pages, then scanned body whitespace into `evidence/page-audit/final-blank-scan.csv`; applying the audit threshold to non-final pages gives `bad_count 0`.
- Generated all-page contact sheets for manual page audit: `evidence/page-audit/clean-all-pages-contact-sheet.png` and `evidence/page-audit/highlighted-all-pages-contact-sheet.png`.

Round1 isolation:
- `02_revision_round1_rework` was restored to the old JPG-based Fig.4/Fig.5 references.
- Round2 source zip contains only the new Fig.4/Fig.5 PDF files for these two figures.
