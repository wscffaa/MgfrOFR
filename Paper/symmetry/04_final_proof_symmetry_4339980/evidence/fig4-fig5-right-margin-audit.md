# Figure 4/5 Right-Margin Audit

Date: 2026-07-10

## Verdict

Do not crop or replace the current Figure 4/5 assets, and do not rebuild the
submission package for this report. The white area shown in the supplied
screenshot is the MDPI manuscript page's right margin, not a large white band
inside either scientific figure.

## Provenance and geometry

- Figure 4 is byte-identical across the Visual Studio Desktop export, Round 2,
  the MDPI production ZIP, and the current proof source. Its embedded JPEG is
  `4110 x 3548`; the right-side raster padding is only `30 px` (`0.73%`).
- Figure 5 uses the same `4110 x 3548` embedded JPEG as the Round 2 landscape
  asset. The production PDF already applies a CropBox that leaves only about
  `28 px` of padding on each horizontal side.
- In the 27-page proof, Figure 5 ends at `x = 535.404 pt` on an A4 page whose
  right edge is `x = 595.276 pt`. The remaining `59.872 pt` is the normal page
  margin. The supplied screenshot was reproduced from this exact page-17
  region.
- The full-width MDPI layout is implemented by
  `adjustwidth{-\extralength}{0cm}` in the production TeX. It expands the
  figure area into the left margin while retaining the journal's right page
  margin.

## Maximum-crop experiment

A temporary, non-promoted build removed all detectable right-side raster
padding from both figure PDFs without changing either embedded JPEG stream.
The build still produced 27 pages. At 2x rendering, the rightmost Figure 5
content moved only from pixel `1052` to pixel `1059`; the visible white region
fell from `139 px` to `132 px`. The page margin remained.

This experiment proves that source-PDF cropping cannot remove the reported
white area. Promoting it would only enlarge/reflow the figures slightly while
leaving the actual margin in place.

## Decision

- Keep both production figure PDFs unchanged.
- Keep the current `manuscript.zip` and `manuscript.pdf` unchanged.
- Do not re-upload an identical or cosmetically misleading package to SuSy.
- Treat any request to remove the remaining white area as an explicit MDPI
  page-layout override, not as image trimming; it requires author approval
  because it would move content outside the validated journal text block.
