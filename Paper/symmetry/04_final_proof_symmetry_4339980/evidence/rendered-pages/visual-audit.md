# Final Proof Visual Audit

> Final acceptance adjudication: **PASS** under the strict whitespace and
> rendering contract. The production-source `[H]` placements were replaced by
> `[t]` for all eight figures after full-document simulations showed that partial
> float changes merely moved the blank-band defect to later pages.

## Locked input

- PDF: `source/symmetry-4339980-english.pdf`
- PDF SHA-256: `35470f614a79fee9661bb5d9ede1d8588bb85128641ff053238e2ee185ec039f`
- TeX SHA-256: `9779e5039cc15bfefcbfbf5ddf2424ca7a36daf00f711b1cd0ba710cf05192a0`
- Corrected Figure 3 SHA-256: `467080bbe051d1f6c1ceb21f8e9e4a06741324895994165c830df1622f3ad0d2`
- Page count: 27
- Render: Ghostscript, 160 dpi, 1323 x 1871 pixels per page
- Independent-build check: the direct source build and the PDF rebuilt from a fresh extraction of `manuscript.zip` have identical extracted-text SHA-256 values and `0/27` rendered-page pixel mismatches.

## Verdict

**PASS: `0` P0 pages and `0` P1 pages.**

- Maximum continuous blank band: page 19, `16.6%`.
- No page exceeds the `18%` manual-review threshold, the `25%` P1 threshold, or the `40%` P0 threshold.
- All eight figures use `[t]`; figure and table numbering and visual order remain monotonic.
- **External production hold — page 1:** the visible production placeholders `Academic Editor: Firstname Lastname`, blank `Published:`, `Symmetry 2026, 1, 0`, and DOI suffix `sym1010000` still require publisher replacement. This is not a clipping or rendering defect and should not be fixed by editing MDPI internal commands.

## Coverage

- Pages 1-27 were rendered and inspected.
- Focus pages 1, 3, 7, 10, 15-20, and 22-27 pass for clipping, overlap, garbled text, and label readability.
- Figures 1-8, Tables 1-5, Equations 1-27, Algorithm 1, declarations, and references were inspected.
- Figure 3 on page 10 passes: corrected dimensions/indexing, equation callouts, centroids label, and ellipsis explanation are visible and legible.
- No blank page, cropped content, overlapping content, garbled glyph, unreadable figure/table label, or rendered `%MDPI`/`%Author` comment was found.
- The build log contains no `LaTeX Error`, undefined reference/citation, fatal error, or overfull box match.

## Page disposition

| Pages | Result | Note |
|---|---|---|
| 1 | PASS + external hold | Layout readable; publisher metadata placeholders remain. |
| 2-18 | PASS | Figures 1-6, Tables 1-3, equations, and surrounding text remain inside bounds and readable. |
| 19 | PASS | Largest continuous blank band, `16.6%`, below all review/block thresholds. |
| 20-27 | PASS | Table 5, Figures 7-8, conclusions, declarations, abbreviations, and references are readable. |

## Evidence

- Individual pages: `page-001.png` through `page-027.png`
- Contact sheets: `contact-01.png` through `contact-07.png`
- Combined contact sheets: `contact-sheets.pdf`
- Pixel audit: `whitespace-audit.tsv`

The visual correction changed only figure placement specifiers; no figure asset, caption, numbering, or scientific result changed.
