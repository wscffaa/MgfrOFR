# Current Resubmission Issue Ledger - 2026-07-01

Scope: `001-reidmamba` Symmetry round-1 rework package.

Verdict: **GO for the local resubmission package gates after the 2026-07-01 repair/revalidation pass.** The original findings are retained below as historical audit records; the active closure status is summarized here.

## 2026-07-01 Closure Status

| Former item | Status | Current evidence |
|---|---|---|
| P0-1 upload package exceeds 120 MB | Closed | Work and final upload sets both total `103,393,460` bytes (`103.393 MB / 98.604 MiB`), below the Symmetry 120 MB total-file limit; see `upload-file-sizes.txt`. |
| P0-2 response/cover overclaim | Closed | Response DOCX, Cover Letter, and Method now agree: no positioning table, no Appendix, no unsupported D1 row, and token initialization is supported by the Method sentence `standard deviation 0.02`; `officecli validate` passed for both DOCX files. |
| P0-3 highlighted-change provenance | Closed | `latexpand --empty-comments` flat regeneration now gives `old_work_cmp=0`, `new_work_cmp=0`, `old_final_cmp=0`, and `new_final_cmp=0`; strict red-delete/blue-add highlighted PDF rebuild passes final log gate with `--no-del` absent. |
| P1 public internal labels | Closed | Clean manuscript, cover, reviewer responses, and response Markdown sources have no public `A0/A1/A2/A3/G1/G2/G4/R1/I1/AG1/D1/D2/F1` row-label residue under word-boundary scan. |
| P1 stale ledgers | Closed | `submission-checklist.md`, `reviewer-coverage-audit-20260701.md`, and `revision-changelog.md` were refreshed to the current package state. |
| P2 implementation default still max fusion | Advisory only | Paper/config release must keep `mgfe_token_fusion: avg` explicit; this is not a local manuscript-package blocker. |

This ledger is based on the current raw artifacts under:

- Work package: `projects/001-reidmamba/Paper/symmetry/02_revision_round1_rework/`
- Final candidate package: `projects/001-reidmamba/Paper/submission_symmetry/revision_round1_rework/`
- First-submission baseline: `projects/001-reidmamba/Paper/symmetry/01_initial_submission/source/MGFROFR.tex`

## Non-negotiable Fusion Source of Truth

The submitted/main model is **F1: MGFE + RATR with average restoration-token fusion**. A3 is **only** the max-fusion ablation/control, not the submitted model.

Evidence:

- `projects/001-reidmamba/Paper/symmetry/02_revision_round1_rework/evidence/f1-average-fusion-freeze-20260701.md:5-8`
- `projects/001-reidmamba/Paper/symmetry/02_revision_round1_rework/evidence/f1-average-fusion-freeze-20260701.md:51-55`
- `projects/001-reidmamba/Exp/registry.yaml:15-18`
- `projects/001-reidmamba/Exp/registry.yaml:245-258`
- `projects/001-reidmamba/Exp/options/test/mgfrofr_f1_synthetic.yml:35`
- `projects/001-reidmamba/Exp/options/test/mgfrofr_f1_davis.yml:35`
- `projects/001-reidmamba/Exp/options/test/mgfrofr_f1_realworld.yml:36`
- `projects/001-reidmamba/Paper/symmetry/02_revision_round1_rework/source/sections/method.tex:114-124`
- `projects/001-reidmamba/Paper/symmetry/02_revision_round1_rework/source/sections/method.tex:361`

Practical rule:

- Public manuscript labels should use module names, not internal IDs.
- `A0/A1/A2/A3/G1/G2/G4/R1/I1/AG1/D1/D2/F1` may appear only in internal evidence ledgers or, if absolutely necessary, in one traceability footnote.
- `max fusion` must be framed as a control proving why average fusion is used, not as the model configuration.

## P0 Findings

### P0-1. Upload package exceeds the Symmetry 120 MB total-file limit

Problem:

The current upload set totals `127,220,368` bytes (`127.220 MB / 121.327 MiB`), above the official Symmetry limit of 120 MB for all uploaded files.

Evidence:

- Official Symmetry instruction page: `https://www.mdpi.com/journal/symmetry/instructions`
- Command:

```bash
python3 - <<'PY'
from pathlib import Path
root=Path('projects/001-reidmamba/Paper/symmetry/02_revision_round1_rework/upload')
files=list(root.iterdir())
total=sum(f.stat().st_size for f in files if f.is_file())
print(f'total_bytes={total}')
print(f'total_MB_decimal={total/1_000_000:.3f}')
print(f'total_MiB={total/1024/1024:.3f}')
for f in sorted(files):
    if f.is_file():
        print(f'{f.name}\t{f.stat().st_size}\t{f.stat().st_size/1_000_000:.3f} MB')
PY
```

Key output:

```text
total_bytes=103393460
total_MB_decimal=103.393
total_MiB=98.604
MGFROFR-clean.pdf                    27.567 MB
MGFROFR-highlighted-changes.pdf      27.704 MB
MGFROFR-latex-source.zip             27.240 MB
Supplementary_Video_S1.mp4           20.656 MB
```

Why it blocks resubmission:

The upload can fail at SuSy, or the editorial office may request a rebuild before review assignment.

Recommended fix:

Reduce total size below 120 MB with margin. First target the largest assets:

- Recompress `Fig4_SOTA_Synthetic_REDS_synthetic_Qualitative_roi_tile_special.jpg` inside the source zip (`21,373,311` bytes uncompressed in zip listing).
- Recompress PDF image streams by rebuilding clean/highlighted PDFs after image compression.
- If still above limit, compress `Supplementary_Video_S1.mp4` further or confirm with the editorial office before upload.
- Re-run `stat`/size check and source-zip rebuild.

### P0-2. Response letters and cover letter still overclaim content that is absent from the current manuscript

Problem:

The response documents and cover letter claim revisions that the current manuscript does not actually contain.

Evidence:

- `officecli view projects/001-reidmamba/Paper/symmetry/02_revision_round1_rework/upload/Response-to-reviewer1-round1.docx text --max-lines 240`
  - R1 Response 1 claims an `architecture x theory difference table`.
  - R1 "Revision made" claims `Added Table 1 (positioning table)`.
  - R1 Response 3 claims `diversity loss (D1)`.
- `officecli view projects/001-reidmamba/Paper/symmetry/02_revision_round1_rework/upload/Response-to-reviewer2-round1.docx text --max-lines 240`
  - R2 Response 5 claims token initialization `std = 0.02` was added to the Method section and Appendix.
- `projects/001-reidmamba/Paper/submission_symmetry/revision_round1_rework/evidence/Cover_Letter_MgfrOFR_Symmetry.tex:27`
  - Cover letter claims an `architecture \times theory difference table`.
- `projects/001-reidmamba/Paper/submission_symmetry/revision_round1_rework/evidence/Cover_Letter_MgfrOFR_Symmetry.tex:41`
  - Cover letter claims token initialization `std = 0.02`.
- Current manuscript scan:

```bash
rg -n "architecture|theory|positioning|D1|diversity loss|std = 0\.02|std=0\.02|Appendix|token initialization|trunc_normal|Table 1" \
  projects/001-reidmamba/Paper/symmetry/02_revision_round1_rework/source/MGFROFR.tex \
  projects/001-reidmamba/Paper/symmetry/02_revision_round1_rework/source/sections \
  projects/001-reidmamba/Paper/symmetry/02_revision_round1_rework/source/references.bib
```

The manuscript has symmetry/architecture prose, but no positioning table, no D1 row, no Appendix, and no explicit token initialization `std = 0.02` in the paper source. The implementation does contain token initialization at `projects/001-reidmamba/archs/mgfe.py:52-53`, but that is not the same as having added it to the manuscript.

Why it blocks resubmission:

Reviewers can directly compare the response letters against the marked manuscript. A promised table/appendix/ablation that is absent looks like a non-response.

Recommended fix:

Choose one path and keep all files synchronized:

- Preferred minimal fix: remove overclaims from both response DOCX and cover letter. Do not promise a positioning table, D1 diversity-loss row, Appendix, or explicit `std = 0.02` manuscript text unless they are actually added.
- If keeping `std = 0.02`, add one concise implementation sentence to Method and update source zip/PDF/highlighted/letters together.
- Do not add D1 or a positioning table unless there is real evidence and space; weaker but truthful wording is safer.

### P0-3. Highlighted-change provenance is not byte-reproducible from the current source and evidence flat files

Problem:

The highlighted-change source says it was generated from:

- `../evidence/MGFROFR-old-first-submission-flat.tex`
- `../evidence/MGFROFR-new-flat.tex`

but regenerating both flat files from the current first-submission and current clean source does not byte-match the work evidence flat files.

Evidence:

- `projects/001-reidmamba/Paper/symmetry/02_revision_round1_rework/source/MGFROFR-highlighted-changes.tex:1-4`
- Command:

```bash
tmpdir=$(mktemp -d /tmp/mgfrofr-flatcheck.XXXXXX)
(cd projects/001-reidmamba/Paper/symmetry/01_initial_submission/source && latexpand --empty-comments MGFROFR.tex) > "$tmpdir/old.tex"
(cd projects/001-reidmamba/Paper/symmetry/02_revision_round1_rework/source && latexpand --empty-comments MGFROFR.tex) > "$tmpdir/new.tex"
cmp -s "$tmpdir/old.tex" projects/001-reidmamba/Paper/symmetry/02_revision_round1_rework/evidence/MGFROFR-old-first-submission-flat.tex; echo old_work_cmp=$?
cmp -s "$tmpdir/new.tex" projects/001-reidmamba/Paper/symmetry/02_revision_round1_rework/evidence/MGFROFR-new-flat.tex; echo new_work_cmp=$?
```

Key output:

```text
old_work_cmp=1
new_work_cmp=1
```

Additional observation:

The inspected diff is mostly formatting/comment-line drift, but the current audit cannot claim byte-level reproducibility.

Why it blocks resubmission:

The editor only needs a marked manuscript, but the package audit asked for provenance against the initial submission. If challenged, the current evidence cannot prove that the highlighted PDF was generated from the exact current clean source and the exact first-submission baseline.

Recommended fix:

Regenerate in one controlled pass:

1. `latexpand --empty-comments` from the initial source directory.
2. `latexpand --empty-comments` from the current clean source directory.
3. Replace the two flat evidence files.
4. Rebuild `MGFROFR-highlighted-changes.tex/pdf` from those flat files.
5. Re-run `cmp`, `latexmk`, `pdfinfo`, and log scans.

## P1 Findings

### P1-1. Public ablation/sensitivity labels still expose internal variant IDs

Problem:

The manuscript still shows internal labels in public-facing tables and captions: `A0/A1/A2/A3`, `G1/G2/G4`, `R1`, `I1`, and `AG1`.

Evidence:

- `projects/001-reidmamba/Paper/symmetry/02_revision_round1_rework/source/sections/results.tex:142-146`
- `projects/001-reidmamba/Paper/symmetry/02_revision_round1_rework/source/sections/results.tex:151`
- `projects/001-reidmamba/Paper/symmetry/02_revision_round1_rework/source/sections/results.tex:156`
- `projects/001-reidmamba/Paper/symmetry/02_revision_round1_rework/source/sections/results.tex:162-165`
- `projects/001-reidmamba/Paper/symmetry/02_revision_round1_rework/source/sections/results.tex:172-179`
- `projects/001-reidmamba/Paper/symmetry/02_revision_round1_rework/source/sections/results.tex:184`

Why it matters:

Reviewer-facing tables should read as module ablations, not experiment ledger IDs. Internal codes make the revision look like a lab notebook and make the average-fusion/max-fusion model selection harder to parse.

Recommended fix:

Use module labels in the visible table rows/captions:

| Current visible label | Recommended visible label |
|---|---|
| `MambaOFR (A0)` | `MambaOFR baseline` |
| `+MGFE only (A1)` | `+MGFE only` |
| `+RATR only (A2)` | `+RATR only` |
| `MgfrOFR (Ours)` | `MgfrOFR` or `MgfrOFR (average fusion)` |
| `A3 max fusion` | `Max-fusion control` or `+max-fusion control` |
| `G1 (4t/1b)` | `4 tokens / 1 branch` |
| `G2 (8t/2b)` | `8 tokens / 2 branches` |
| `MgfrOFR (12t/3b, avg)` | `MgfrOFR, 12 tokens / 3 branches` |
| `G4 (16t/4b)` | `16 tokens / 4 branches` |
| `R1 ($\tau{=}0.05$)` | `Lower ranking temperature ($\tau{=}0.05$)` |
| `I1 (prepend insertion)` | `Prepend token insertion` |
| `AG1 (max aggregation)` | `Max branch aggregation` |

If traceability is needed, use one footnote:

`Internal IDs: baseline = A0, +MGFE only = A1, +RATR only = A2, max-fusion control = A3; the submitted MgfrOFR model is F1 average fusion.`

Do not put internal IDs in primary row labels or figure subpanel labels.

### P1-2. The ablation visual caption should follow modular subfigure naming

Problem:

The current Figure 6 caption still says columns compare `MambaOFR (A0), +MGFE only (A1), +RATR only (A2), and MgfrOFR (Ours)`, and separately says A3 is omitted.

Evidence:

- `projects/001-reidmamba/Paper/symmetry/02_revision_round1_rework/source/sections/results.tex:156`

Why it matters:

The caption should match the standard module-comparison form shown in the user's example: `(a) Input`, `(b) +LHFM only`, `(c) +FGM only`, etc. The visible labels should communicate components, not internal experiment IDs.

Recommended fix:

Use figure labels/caption language like:

- `(a) Input`
- `(b) MambaOFR baseline`
- `(c) +MGFE only`
- `(d) +RATR only`
- `(e) MgfrOFR`
- `(f) Ground truth`

Caption sentence:

`The restoration columns compare the MambaOFR baseline, +MGFE only, +RATR only, and MgfrOFR with average fusion; the max-fusion control is omitted for visual clarity.`

### P1-3. Internal evidence ledgers contain stale or over-optimistic conclusions

Problem:

Internal evidence files still say all reviewer comments are answered and no residual risk remains, but current raw artifacts contradict that.

Evidence:

- `projects/001-reidmamba/Paper/symmetry/02_revision_round1_rework/evidence/reviewer-coverage-audit-20260701.md:5`
- `projects/001-reidmamba/Paper/symmetry/02_revision_round1_rework/evidence/reviewer-coverage-audit-20260701.md:43-45`
- `projects/001-reidmamba/Paper/symmetry/02_revision_round1_rework/evidence/revision-changelog.md:13`
  - stale claim: Wilcoxon significance only for PSNR/SSIM, LPIPS/DISTS non-significant.
- Current manuscript/evidence says all four metrics are significant:
  - `projects/001-reidmamba/Paper/symmetry/02_revision_round1_rework/source/sections/results.tex:76`
  - `projects/001-reidmamba/Paper/symmetry/02_revision_round1_rework/evidence/f1-average-fusion-freeze-20260701.md:44-49`

Why it matters:

These files are not necessarily uploaded, but they are dangerous if used for final editorial handoff or future regeneration. They also caused the exact failure mode this audit is preventing: old conclusions replacing current raw artifacts.

Recommended fix:

Update or supersede stale evidence files after the actual source/DOCX/PDF fixes. Mark older audit files as superseded rather than deleting them.

### P1-4. Response letters still use internal decision language

Problem:

The response letters contain internal model-selection language (`D2`, `A3-family`, `I1/AG1 frozen`) that is understandable inside the project but not ideal for reviewer-facing prose.

Evidence:

- `officecli view ... Response-to-reviewer1-round1.docx text --max-lines 240`
  - R1 response text includes `D2 model-selection decision`, `D2 decision record`, `A3-family controls`, `I1/AG1`.
- `officecli view ... Response-to-reviewer2-round1.docx text --max-lines 240`
  - R2 response text includes `D2 model-selection review`, `G1/G2/G4`, `I1/AG1`.

Why it matters:

Even if scientifically correct, this reads like internal project management rather than an author response. It also makes average-fusion as the main model less clean.

Recommended fix:

Translate internal IDs to reviewer-facing terms:

- `D2 model-selection decision` -> `the final model-selection audit`
- `A3-family controls` -> `predefined max-fusion controls`
- `I1/AG1` -> `token-insertion and branch-aggregation controls`
- `G1/G2/G4` -> `one-, two-, and four-branch granularity controls`
- `F1` -> avoid in DOCX unless in one traceability sentence.

### P1-5. Source zip compile log contains first-pass undefined citation/reference warnings; final pass is clean but the verification wording should be precise

Problem:

`source-zip-rebuild-20260701.log` contains first-pass undefined citation/reference warnings, followed by reruns and final success.

Evidence:

- `projects/001-reidmamba/Paper/symmetry/02_revision_round1_rework/evidence/source-zip-rebuild-20260701.log:997-1018`
- `projects/001-reidmamba/Paper/symmetry/02_revision_round1_rework/evidence/source-zip-rebuild-20260701.log:1366-1375`

Why it matters:

This is not a compile blocker because `latexmk` reran and ended with `All targets () are up-to-date`, but a naive `rg` over the full log will report warnings. Verification text must say "final latexmk pass clean" rather than "the whole raw log has no undefined warnings".

Recommended fix:

Keep the log, but add a final-pass log extract or scan the final generated `.log` after latexmk completes.

## P2 Findings

### P2-1. Clean and highlighted PDFs are both 27 pages, and stale ledgers have been refreshed

Evidence:

- Command:

```bash
/Users/caifeifan/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/pdfinfo \
  projects/001-reidmamba/Paper/symmetry/02_revision_round1_rework/upload/MGFROFR-clean.pdf
/Users/caifeifan/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/pdfinfo \
  projects/001-reidmamba/Paper/symmetry/02_revision_round1_rework/upload/MGFROFR-highlighted-changes.pdf
```

Key output:

```text
MGFROFR-clean.pdf: Pages: 27
MGFROFR-highlighted-changes.pdf: Pages: 27
```

Former stale evidence, now refreshed:

- `projects/001-reidmamba/Paper/symmetry/02_revision_round1_rework/evidence/revision-changelog.md:38`
- `projects/001-reidmamba/Paper/symmetry/02_revision_round1_rework/evidence/reviewer-coverage-audit-20260701.md:10`

Recommended fix:

After regenerating highlighted changes, update the page count in the audit ledgers.

### P2-2. `submission-checklist.md` package size is stale

Evidence:

- `projects/001-reidmamba/Paper/symmetry/02_revision_round1_rework/evidence/submission-checklist.md:34` says `127,067,759` bytes.
- Current command output says `127,220,368` bytes.

Recommended fix:

Regenerate the size table after package compression.

### P2-3. Implementation default still says max fusion, so release configs must remain explicit

Problem:

`projects/001-reidmamba/archs/mgfe.py:39` defaults `token_fusion` to `max`, although F1 test configs explicitly set `mgfe_token_fusion: avg`.

Evidence:

- `projects/001-reidmamba/archs/mgfe.py:39`
- `projects/001-reidmamba/Exp/options/test/mgfrofr_f1_synthetic.yml:35`
- `projects/001-reidmamba/Exp/options/test/mgfrofr_f1_davis.yml:35`
- `projects/001-reidmamba/Exp/options/test/mgfrofr_f1_realworld.yml:36`

Why it matters:

This is not a manuscript blocker if every released config sets `avg`, but public code users may instantiate the module directly and get max fusion. That can recreate the average/max confusion.

Recommended fix:

For paper resubmission, ensure all released configs explicitly set `mgfe_token_fusion: avg`. For code release, consider changing the default to `avg` only if backward compatibility is not a concern.

## Confirmed Passes / Do Not Re-litigate

These items currently pass and should not be reopened unless files change.

| Check | Current status | Evidence |
|---|---|---|
| Main model fusion | Pass: F1 average fusion is the submitted model; A3 is a max-fusion control | `f1-average-fusion-freeze-20260701.md:5-8`, `Exp/registry.yaml:245-258`, `method.tex:114-124` |
| Clean/source zip consistency | Pass: source zip matches current source for key files | `cmp` output: `MGFROFR.tex cmp=0`, `sections/results.tex cmp=0`, `sections/method.tex cmp=0`, `sections/discussion.tex cmp=0`, `sections/conclusion.tex cmp=0`, `references.bib cmp=0` |
| Work upload vs final candidate upload | Pass: file SHA256 values match for all 7 upload files | `shasum -a 256` over both upload directories; identical hashes for clean PDF, highlighted PDF, source zip, cover letter, two response DOCX, and video |
| DOCX schema | Pass | `officecli validate` returned `Validation passed: no errors found.` for both response DOCX files |
| Standalone `OFR` terminology | Pass in clean source and response DOCX text | `rg -n -P '(?<![A-Za-z])OFR(?![A-Za-z])' ...` returned no matches |
| Real-world CLIP-IQA+ framing | Pass: manuscript does not claim CLIP-IQA+ improvement over MambaOFR | `results.tex:103`, `discussion.tex:50`, `conclusion.tex:6` |
| Source zip includes required LaTeX assets | Pass | `unzip -l MGFROFR-latex-source.zip` lists `MGFROFR.tex`, `references.bib`, all section files, figures, and MDPI Definitions; 28 files total |

## Required Repair Plan

1. Fix public labels in `results.tex`.
   - Replace visible `A0/A1/A2/A3/G1/G2/G4/R1/I1/AG1` labels with module/descriptive labels.
   - Keep one optional traceability footnote only if needed.
   - Preserve the average-fusion main-model message.

2. Fix response DOCX and cover letter overclaims.
   - Remove positioning-table, D1, Appendix, and unsupported `std = 0.02 in manuscript` claims unless actually added.
   - Rewrite internal decision IDs into reviewer-facing prose.

3. Regenerate clean PDF, highlighted PDF, source zip, and cover letter PDF.
   - Re-run `latexpand` from correct source directories.
   - Re-run `latexdiff`/highlighted build from the regenerated flats.
   - Rebuild source zip from current source.

4. Reduce upload size below 120 MB.
   - Compress the largest figure/PDF/video assets.
   - Recompute total bytes and SHA256.

5. Refresh evidence ledgers.
   - Supersede stale `reviewer-coverage-audit-20260701.md` and `revision-changelog.md`.
   - Update page counts and package size.
   - Keep old files only as history, not current readiness evidence.

6. Final validation commands.

```bash
# clean manuscript
latexmk -pdf -interaction=nonstopmode -halt-on-error MGFROFR.tex

# highlighted manuscript
latexmk -pdf -interaction=nonstopmode -halt-on-error MGFROFR-highlighted-changes.tex

# source zip independent build
tmpdir=$(mktemp -d /tmp/mgfrofr-sourcezip.XXXXXX)
unzip -q upload/MGFROFR-latex-source.zip -d "$tmpdir"
(cd "$tmpdir" && latexmk -pdf -interaction=nonstopmode -halt-on-error MGFROFR.tex)

# DOCX validation
officecli validate upload/Response-to-reviewer1-round1.docx
officecli validate upload/Response-to-reviewer2-round1.docx

# terminology and internal-ID gates
rg -n -P '(?<![A-Za-z])OFR(?![A-Za-z])' source upload
rg -n 'A0|A1|A2|A3|G1|G2|G4|R1|I1|AG1|D1|D2|F1' source upload

# upload size and SHA sync
python3 - <<'PY'
from pathlib import Path
root=Path('upload')
print(sum(f.stat().st_size for f in root.iterdir() if f.is_file()))
PY
shasum -a 256 upload/* ../../submission_symmetry/revision_round1_rework/upload/*
```

## Editor-Style Recommendation

The package can proceed to the SuSy upload step after a final human slot check in the portal. The former editorial blockers are closed: package size is below the official limit, response/cover-letter claims match the manuscript, highlighted-change provenance is byte-reproducible from regenerated flats, and public ablation/sensitivity labels use modular descriptions rather than internal IDs.
