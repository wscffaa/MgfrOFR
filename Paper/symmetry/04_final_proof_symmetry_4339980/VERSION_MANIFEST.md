# Symmetry 4339980 Final Proof Manifest

## Lifecycle state

- Manuscript: `symmetry-4339980`
- SuSy stage: `Author proofreading`
- Accepted: `09 July 2026`
- Package date: `11 July 2026`
- Current verdict: `CONDITIONAL-GO` -- all content, number, build, visual, attachment, repository-publicity, and five upload-slot gates pass; final review of the live confirmation/e-mail controls and final Submit remain human-only.

## Source lineage

| Artifact | SHA-256 | Role |
|---|---|---|
| `original/symmetry-4339980.zip` | `ef482095bd96a0ae6b8f915eeb69f8299d71a02b66f87dfc5660b0a9de1e97e7` | Immutable SuSy production download |
| Production TeX inside original ZIP | `73c657f6f224ece246bd2289754cbb031151bbe08fe9b711e1eadde773a7567c` | Only editable proof baseline |
| `source/symmetry-4339980-english.tex` | `d5e685c98c61a7432615d415ee8b55e9cbfb531fc575e5877f6ad16386be1d8b` | Final answered English-editor closure source |
| `source/symmetry-4339980-english.pdf` | `7f33ec06185060db77868514a47d8b279ce10f4679173ddb09ba37afc5ec9c4c` | PDF from an independent extraction/build of the upload ZIP, 28 A4 pages |
| `source/figures/Fig3_ratr_module_detail.pdf` | `467080bbe051d1f6c1ceb21f8e9e4a06741324895994165c830df1622f3ad0d2` | Corrected Figure 3 vector export |

The Qi Zhang ORCID is aligned with project 007 final proof: `0009-0008-9432-7018`. The rejected old value `0000-0002-3827-1522` remains only in the preserved MDPI query text and is not active author metadata.

## Proof contract

- Query gate: `23 %MDPI / 23 %Author / 0 orphan`.
- Highlight gate: all original `53 \hl{}` markers retained; `3 \highlighting{}` markers include the verified ORCID correction.
- Content structure: 27 equations, 9 equation labels, 8 figures, and 5 tables.
- Number gate: the production-to-pre-closure gate remains `PASS`; the pre-closure-to-final gate contains exactly one authorized deletion (`7.6%`) and no addition, with the remaining `953` numeric tokens in exact order.
- Complexity provenance: the frozen cross-method benchmark and separate paired sanity benchmark are now explicitly distinguished; no complexity value changed.
- Repository gate: `wscffaa/MgfrOFR` is `PUBLIC`; anonymous HTTP returned `200` and credential-free `git ls-remote` resolved `HEAD` to `d4a1adab6c4cda38962a826e357cdc5497eaf71c`.
- Visual gate: 28 pages under controlled floating; the maximum non-exempt continuous blank band is `24.8%`, below the `25%` threshold. Page 25's `34.0%` back-matter transition is exempt because the following Abbreviations block is indivisible.

## Submission-ready artifacts

| SuSy slot / local artifact | Bytes | SHA-256 | Web state |
|---|---:|---|---|
| `submission_ready/manuscript.zip` | 13,438,207 | `4152460d8e7252c4324582b5b03b3c30efc7015a0ce4029c09d939f64ac85696` | `100%`, no error |
| `submission_ready/manuscript.pdf` | 13,397,653 | `7f33ec06185060db77868514a47d8b279ce10f4679173ddb09ba37afc5ec9c4c` | `100%`, no error |
| `submission_ready/manuscript-supplementary.zip` | 20,655,867 | `934d2aaaba4dd67cf906a7b776516d17be649aa64dc3a6da76e1cd9a7de520fd` | `100%`, no error |
| `submission_ready/non_published_material.v2.pdf` | 13,358,908 | `bc8d7f66b1ac15ce6c579e26367bad72b09244cabad183993c9921c0d115ff1a` | `100%`, no error |
| `submission_ready/coverletter-final-proof.pdf` | 95,399 | `f3ba6c13627d5088ad76741195fdf349029e7eb0e060d17526360afd13a7341f` | `100%`, no error |

SuSy's Supplementary component rejects `.mp4` through a hard-coded front-end allowlist. The accepted ZIP is an uncompressed, one-file transport wrapper. Its inner `manuscript-supplementary.mp4` is byte-identical to the SuSy download and remains separately available in `submission_ready/` at `20,655,713` bytes with SHA-256 `43efb7c7a88fdaf12e3d8bf3b1a12e2a2bae38195ac556082d5dc6fc98e56130`.

Figures/Graphics and Graphical Abstract are intentionally empty. The Round 2 `coverletter.v3.pdf` is retained locally only as superseded provenance and is no longer the live Cover Letter. At 02:21 CST on 11 July 2026, SuSy showed `coverletter-final-proof.pdf` at `100%`, `uploading=false`, and `error=false`. The three final proof confirmations and the name `feifan cai` were already present when this replacement was read back; the agent did not alter them and did not click final `Submit`.
