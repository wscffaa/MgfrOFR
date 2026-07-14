# SuSy Upload Readback

Read back from the live author-proofreading page on 10 July 2026.

| Slot | Filename | Browser-reported bytes | Percent | Uploading | Error |
|---|---|---:|---:|---|---|
| Manuscript (Word/ZIP/RAR) | `manuscript.zip` | 13,436,039 | 100 | false | false |
| Manuscript (PDF Version) | `manuscript.pdf` | 13,395,167 | 100 | false | false |
| Supplementary File(s) | `manuscript-supplementary.zip` | 20,655,867 | 100 | false | false |
| Figures, Graphics, Images | empty | -- | -- | -- | -- |
| Graphical Abstract | empty | -- | -- | -- | -- |
| Non-published Material | `non_published_material.v2.pdf` | 13,358,908 | 100 | false | false |
| Cover Letter | `coverletter.v3.pdf` | 127,089 | 100 | false | false |

The direct MP4 selection was rejected locally by SuSy before upload with `File type not allowed`. The component has an empty slot-specific `accept` value but falls back to a hard-coded `.doc/.docx/.pdf/.eml/.jpg/.png/.zip/.rar` allowlist. A zero-compression ZIP wrapper was therefore used; the inner MP4 SHA-256 remains `43efb7c7a88fdaf12e3d8bf3b1a12e2a2bae38195ac556082d5dc6fc98e56130`.

Final controls:

- `cb_author_public_email_1`: checked (Feifan Cai)
- `cb_author_public_email_2`: unchecked (Qi Zhang)
- `cb_author_public_email_3`: unchecked (Kun Yang)
- `cb_author_public_email_4`: unchecked (Lei Chen)
- `cb_author_public_email_5`: checked and system-disabled (Youdong Ding)
- Publication-notification e-mail: blank
- `confirm_proof_author`, `confirm_proof_terms`, `confirm_proof_coauthor`, `confirm_proof`: all unchecked
- Both confirmation-name fields: blank
- `Confirm and Continue`: not clicked
- Final `Submit`: not clicked

The Manuscript ZIP and PDF were each replaced with one upload trigger after all local gates passed. The Supplementary, Figures, Graphical Abstract, Non-published Material, and Cover Letter slots were not retriggered.

Full-page closure evidence: `raw/susy-author-proofreading-after-closure.png` (SHA-256 `0856376faa7c0fb62c4167ff867279b2e0bc4c90cea19ee7cd4f11f06f149e30`).

## Explicit five-slot re-upload and readback -- 11 July 2026, 00:04 CST

At the author's explicit request, all five populated Step 2 slots were uploaded
again from `submission_ready/`, strictly one slot at a time. Each upload was
allowed to finish before the next slot was triggered.

| Slot | Filename | Local/browser bytes | Local SHA-256 | Percent | Uploading | Error | New SuSy `hashKey` |
|---|---|---:|---|---:|---|---|---|
| Manuscript (Word/ZIP/RAR) | `manuscript.zip` | 13,436,039 | `6fe56b7c2b4d45d0f9e8623690ea1af795cb20ec1649bc7571a291bcfb6c8cc4` | 100 | false | false | `70575a5c15c04ed1960819718b12befa` |
| Manuscript (PDF Version) | `manuscript.pdf` | 13,395,167 | `1fb256cd00f09c1db4f61fd754de807cac06e46d6347d2f52c5df0699d09bdb1` | 100 | false | false | `5da7907877b94cb785f7f6a80ef5fa32` |
| Supplementary File(s) | `manuscript-supplementary.zip` | 20,655,867 | `934d2aaaba4dd67cf906a7b776516d17be649aa64dc3a6da76e1cd9a7de520fd` | 100 | false | false | `4c3364779054472f9a4fb174e1e31f69` |
| Figures, Graphics, Images | empty | -- | -- | -- | -- | -- | -- |
| Graphical Abstract | empty | -- | -- | -- | -- | -- | -- |
| Non-published Material | `non_published_material.v2.pdf` | 13,358,908 | `bc8d7f66b1ac15ce6c579e26367bad72b09244cabad183993c9921c0d115ff1a` | 100 | false | false | `3ae9ea8d9d904e7e9aeea5a08a3294e1` |
| Cover Letter | `coverletter.v3.pdf` | 127,089 | `e5299c09def31d933f6099ef8fbffdcce7e72427d2db78651a64a32da33f304f` | 100 | false | false | `9a8fe077d07c4b5682bfe28bd3d338f9` |

The page remained at `Author proofreading`. The upload pass targeted only the
five file inputs; no confirmation, name, e-mail-display, navigation, or submit
control was clicked or edited.

At this readback, the page itself showed a state different from the earlier
closure snapshot: all five public-email boxes were checked; all four proof
confirmation boxes were checked; and both confirmation-name fields contained
`feifan cai`. These controls were left exactly as found. The final `Submit`
button was not clicked.

Evidence:

- `raw/susy-step2-viewport-after-reupload-20260710.png` (SHA-256 `a3e35019ee0fb84201153eb8a5a052e6ab9dc9dfd6d555b3de6856080f9b540c`)
- `raw/susy-step2-lower-after-reupload-20260710.png` (SHA-256 `94ee3049c8275dc1e603fb7a1ca04196f6cf0250c535f28d35177713ae51ab58`)

## Final English-editor closure upload -- 11 July 2026, 01:59 CST

This readback supersedes the earlier live-file and confirmation-control snapshots. The five populated Step 2 slots were uploaded sequentially from the final `submission_ready/` package. A direct MP4 selection was rejected with `File type not allowed`; the verified one-file ZIP wrapper was then uploaded successfully.

| Slot | Filename | Local/browser bytes | Local SHA-256 | Derived percent | Uploading | Error | SuSy `hashKey` |
|---|---|---:|---|---:|---|---|---|
| Manuscript (Word/ZIP/RAR) | `manuscript.zip` | 13,438,207 | `4152460d8e7252c4324582b5b03b3c30efc7015a0ce4029c09d939f64ac85696` | 100 | false | false | `27404b589fd0484b969f55b6a376c5f0` |
| Manuscript (PDF Version) | `manuscript.pdf` | 13,397,653 | `7f33ec06185060db77868514a47d8b279ce10f4679173ddb09ba37afc5ec9c4c` | 100 | false | false | `7f1d3f5de8934012ab614bbb11727968` |
| Supplementary File(s) | `manuscript-supplementary.zip` | 20,655,867 | `934d2aaaba4dd67cf906a7b776516d17be649aa64dc3a6da76e1cd9a7de520fd` | 100 | false | false | `cfd4d995f7b7439188fdf0fda309a3f0` |
| Figures, Graphics, Images | empty | -- | -- | -- | -- | -- | -- |
| Graphical Abstract | empty | -- | -- | -- | -- | -- | -- |
| Non-published Material | `non_published_material.v2.pdf` | 13,358,908 | `bc8d7f66b1ac15ce6c579e26367bad72b09244cabad183993c9921c0d115ff1a` | 100 | false | false | `33bad152cfe74e5287b91343c769dc7e` |
| Cover Letter | `coverletter.v3.pdf` | 127,089 | `e5299c09def31d933f6099ef8fbffdcce7e72427d2db78651a64a32da33f304f` | 100 | false | false | `705b497776f745ebb1b6a71dfc785194` |

The uploader hides the progress widget after completion. The readback computes `100%` from `progress >= size` and additionally requires `uploading=false`, `error=false`, a non-empty `hashKey`, and an exact filename/byte-size match.

Final boundary readback:

- `confirm_proof_terms`, `confirm_proof_coauthor`, and `confirm_proof`: all unchecked.
- Confirmation-name field: blank.
- Publication-notification e-mail: blank.
- Final `Submit`: not clicked.
- Step 1 author information/confirmation: not edited in this upload pass.

Evidence:

- `raw/susy-step2-upload-slots-final-20260711.png` (SHA-256 `658f5a84c653a291eb71cc9887ead3c97c72aad490c477789b120c6d5060cbff`)
- `raw/susy-step2-final-confirmation-boundary-20260711.png` (SHA-256 `f3b32b7ef4936f1583288a1817d246c53acc50f7a060fc965672186ce3e3c681`)

## Proof Cover Letter replacement -- 11 July 2026, 02:21 CST

The previous `coverletter.v3.pdf` was identified as the 8 July Round 2 letter and removed only from the live Cover Letter component. It was replaced with the new Proof-specific PDF.

| Slot | Filename | Local/browser bytes | Local SHA-256 | Derived percent | Uploading | Error | SuSy `hashKey` |
|---|---|---:|---|---:|---|---|---|
| Cover Letter | `coverletter-final-proof.pdf` | 95,399 | `f3ba6c13627d5088ad76741195fdf349029e7eb0e060d17526360afd13a7341f` | 100 | false | false | `be237201d38f44f493d2e1f0c740f764` |

Unchanged slot identities after the replacement:

- Manuscript ZIP: `27404b589fd0484b969f55b6a376c5f0`.
- Manuscript PDF: `7f1d3f5de8934012ab614bbb11727968`.
- Supplementary ZIP: `cfd4d995f7b7439188fdf0fda309a3f0`.
- Non-published Material: `33bad152cfe74e5287b91343c769dc7e`.
- Figures/Graphics and Graphical Abstract: empty.

At this latest readback, the three proof confirmations were checked and the confirmation-name field contained `feifan cai`. Those values were already present and were not changed during the Cover Letter replacement. Final `Submit` remains unclicked.

Evidence: `raw/susy-coverletter-final-proof-replacement-20260711.png` (SHA-256 `1c7b14528eebd1d0cc4acedb6b87cf60c4a9f6c431124a1a77a14fde6dc044d5`).
