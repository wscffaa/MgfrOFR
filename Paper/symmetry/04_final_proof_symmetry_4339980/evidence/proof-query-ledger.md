# MDPI Proof Query Ledger

Source: `../source/symmetry-4339980-english.tex`

Norm aligned with project 007 final proof:

- Preserve every production `%MDPI` query and all editor highlights.
- Answer every query with a following `%Author:` reply before the next `%MDPI` query.
- Apply the requested correction or explicitly confirm the production edit.
- Keep comments non-rendering and stop before the author confirmation/Submit actions.

Gate result: `23 %MDPI / 23 %Author / 0 orphan`; original `53 \hl{}` highlights are retained, and `3 \highlighting{}` markers are present, including the verified Qi Zhang ORCID correction. Four non-query `%Author general note:` comments record the production-placeholder hold, float correction, complexity-snapshot disclosure, and authorized removal of an unsupported exact training-time value.

| ID | Source line | Topic | Resolution and evidence | Status |
|---|---:|---|---|---|
| Q01 | 35--36 | Names and affiliations | Checked the accepted author order and affiliation map; the adjacent reply confirms them as shown. | Resolved |
| Q02 | 37--38 | Qi Zhang ORCID | Did not restore the rejected `0000-0002-3827-1522`; replaced it with the project-007-verified matching iD `0009-0008-9432-7018` and retained a highlighted ORCID marker. | Resolved |
| Q03 | 44--45 | Author e-mails | Confirmed the four production-added addresses for F.C., Q.Z., K.Y., and L.C. | Resolved |
| Q04 | 52--53 | Abbreviations | Completed a three-scope audit: the abstract independently defines MgfrOFR/SRWOV; the main text defines every non-proper-name acronym at first use; and the first affected figure/table independently defines its displayed acronyms, including Figure 1 DCN/Concat, Table 1 methods/metrics, Figure 4 ROI/GT, Table 5 FP32/FLOPs/FPS, and Figure 8 MAE. Corrected REDS to `REalistic and Dynamic Scenes`. | Resolved |
| Q05 | 115--116 | Figure conventions | Added the meaning of colors, solid/dashed arrows, dashed boxes, ROI boxes, and training-only paths; also recorded the verified change of all figures from fixed to top-page floating placement. | Resolved |
| Q06 | 166--169 | Hardware/software provenance | Added NVIDIA manufacturer/location, retained PyTorch 2.7 and CUDA 12.4, and added the official pyiqa URL with `10 July 2026` access date. | Resolved |
| Q07 | 193--194 | Equations | Rechecked all 27 displayed equations, 9 formula labels, variable typography, numbering, and references; also aligned Figure 3's embedded equation references and symbols. | Resolved |
| Q08 | 349--350 | Figure 3 ellipses | Explained that ellipses denote omitted negative candidates for visual clarity and not missing scientific content. | Resolved |
| Q09 | 468--469 | Standard-format edit | Confirmed and retained `Both`. | Resolved |
| Q10 | 487--488 | Bold formatting | Confirmed the two bold inline lead-ins are intentional paragraph-level headings. | Resolved |
| Q11 | 489--490 | Italic formatting | Removed unnecessary narrative emphasis from both `outcome` and `consequence`; retained italics only for subgroup headings, mathematical notation, and required reference formatting. | Resolved |
| Q12 | 567--568 | Metric arrows | Added the higher/lower-is-better explanation to all five affected table captions. | Resolved |
| Q13 | 627--628 | Figure 4 clarity | Verified `4110 x 3548`, 600 dpi, readable scientific content, and clarified the ROI boxes; no replacement needed. | Resolved |
| Q14 | 642--643 | Figure 5 clarity | Verified `4110 x 3548`, 600 dpi, readable scientific content, and clarified the ROI boxes; no replacement needed. | Resolved |
| Q15 | 644--645 | Figure 5 non-English mark | Explained that `PATHÉ` is an archival source watermark, not untranslated manuscript text or a restoration artifact. | Resolved |
| Q16 | 709--710 | Table group italics | Confirmed italics intentionally distinguish the two predefined sensitivity-control row groups. | Resolved |
| Q17 | 815--816 | Threat labels | Confirmed bold labels intentionally distinguish five threat categories in one paragraph. | Resolved |
| Q18 | 851--852 | Data-availability date | Added `accessed on 10 July 2026` and verified the repository is publicly accessible without authentication. | Resolved |
| Q19 | 855--856 | Codex website | Added `https://openai.com/codex/` and retained `accessed on 1 July 2026` without expanding the disclosed AI-use scope. | Resolved |
| Q20 | 901--902 | CVPR location/date | Confirmed the production-added New Orleans location and `18--24 June 2022` dates. | Resolved |
| Q21 | 903--904 | IEEE publisher | Confirmed IEEE as the publisher and retained the production edit. | Resolved |
| Q22 | 926--927 | COLM entry | Confirmed the normalized reference, removed unnecessary information, and retained the verified location/dates. | Resolved |
| Q23 | 1260--1261 | DeOldify entry | Confirmed removal of `GitHub repository`; retained the project title, year, URL, and access date. | Resolved |

General production note: line 23 asks MDPI to replace the placeholder editor, volume/issue/article number, publication date, and DOI without modifying MDPI internal commands.
