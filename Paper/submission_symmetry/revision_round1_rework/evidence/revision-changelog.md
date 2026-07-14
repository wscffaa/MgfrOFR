# Round-1 Revision Changelog

Scope: all changes in this reworked upload candidate relative to the round-1 first submission (2026-05-11). Per-reviewer-comment mapping is in `reviewer-coverage-audit-20260701.md`.

Last updated: 2026-07-01.

## Manuscript sections (`sections/*.tex`, `MGFROFR.tex`)

- **abstract.tex** — Rewritten around multi-granularity feature decomposition + ranking-aware regularization; frames the contribution as representation-level branch balance under heterogeneous, asymmetric degradation.
- **introduction.tex** — Restructured to the representation-level symmetry framing; explicit RTN/RRTN/MambaOFR positioning; four-point MGFE/RATR contribution list; shortened per R2-C6.
- **related_work.tex** — Reorganized into old film restoration, state-space models, multi-granularity representation, and ranking/diversity regularization; added diffusion/foundation-prior restoration (DiffBIR/SUPIR/SeeSR) as non-old-film-restoration context; sharpened novelty statement per R1-C1.
- **method.tex** — Rewritten Problem Setup / Input Representation / MGFE / RATR; average fusion is the submitted default (max→average correction); token insertion and truncated-normal initialization (standard deviation 0.02) made explicit per R2-C5.
- **results.tex** — Two-setting evaluation kept apart (synthetic full-reference vs. real-world no-reference); seven metrics; 30-clip synthetic + 216-clip real-world SRWOV protocol; Wilcoxon significance reported for PSNR/SSIM/LPIPS/DISTS under the paired 30-clip protocol; descriptive token-insertion and branch-aggregation controls; Fig 4/5 restored to full-method panels; Supplementary Video S1 referenced.
- **discussion.tex** — Four explicit differences vs. MambaOFR; perception–distortion analysis of the MGFE-only vs. full model gap; branch-similarity / error-map evidence for the symmetry claim.
- **conclusion.tex** — Contribution summary; limitations incl. RATR training-time cost (~7.6% over MambaOFR) and SRWOV-only evaluation scope.
- **MGFROFR.tex** — `\supplementary{}` now declares Video S1 (two-part); previously `Not applicable.`

## Symmetry-scope reinforcement (Symmetry-journal fit)

Restored the Symmetry-journal framing that an earlier rewrite had thinned out, so the introduction → related work → method §3.7 symmetry argument chain stays intact. Basis: MDPI Symmetry image-restoration/DL convention (symmetry framed as an architectural/theoretical prior; permutation invariance treated as a standard group symmetry, per geometric deep learning).

- **introduction.tex** — Added that the branch-diversity objective is invariant under permutations of the granularity branches (the symmetric group $\mathcal{S}_G$), i.e. a permutation symmetry / standard group-symmetry principle rather than a geometric one, placing MgfrOFR within symmetry-driven representation learning for image restoration.
- **related_work.tex** (`subsec:symmetry_ai`) — Linked the representation symmetry to the two group invariances proved in method §3.7: branch-permutation invariance under $\mathcal{S}_G$ and direction-exchange invariance under the bidirectional $\mathbb{Z}_2$ action.
- **related_work.tex** — Folded the deleted tabular positioning claim into one prose sentence (MgfrOFR is the only compared design whose branch structure carries an explicit permutation-and-exchange symmetry rather than acting on feature magnitude alone).

## Supplementary Video S1 (new)

- Replaces the earlier real-world-only clip. Two parts, unified panel style (dark label bar, MgfrOFR highlighted in green, metric annotated):
  - **Part 1 — REDS-synthetic, 4 panels** `Input | MambaOFR | MgfrOFR | GT` with **per-frame PSNR**. Clips 004 (mean ΔPSNR +5.88 dB) and 010 (+3.00 dB), data-selected as the strongest MgfrOFR-over-MambaOFR advantage.
  - **Part 2 — real-world SRWOV, 3 panels** `Input | MambaOFR | MgfrOFR` with **overall no-reference NIQE/BRISQUE** (MgfrOFR 5.12/24.79 vs. MambaOFR 5.34/29.79, from Table `tab:realworld`).
- Encoding: H.264 / yuv420p, 1934×444, 12 fps, 37.4 s, 20,655,713 bytes. MDPI-compliant.

## Upload package (`upload/`)

| File | State |
|---|---|
| `MGFROFR-clean.pdf` | 27 pages, log gate clean |
| `MGFROFR-highlighted-changes.pdf` | 32 pages, strict red-delete/blue-add `latexdiff` from byte-reproducible flats vs. `symmetry/01_initial_submission/source/`; `--no-del` absent; log gate clean |
| `MGFROFR-latex-source.zip` | Independently rebuilds to 27 pages |
| `Response-to-reviewer1-round1.docx` | Internal IDs and unsupported table/extra-panel claims removed; `officecli validate` passed |
| `Response-to-reviewer2-round1.docx` | Internal IDs removed; R2-C5 now matches the Method token-initialization sentence; `officecli validate` passed |
| `Cover-Letter.pdf` | Rebuilt; R2-C5 token-initialization summary matches Method |
| `Supplementary_Video_S1.mp4` | Two-part synthetic+real-world video (new) |

## Validation

- Clean, source-zip, and highlighted TeX logs return no LaTeX error / unresolved reference / unresolved citation / rerun warning.
- Highlighted diff uses `PICTUREENV` protection plus highlighter-only compatibility labels/bibliography for deleted old-side refs, so red deletions remain visible while the diff compiles clean.
- Both response DOCX validate against the OpenXML schema.
- `upload-sha256.txt` verifies file-by-file against the current upload set.
