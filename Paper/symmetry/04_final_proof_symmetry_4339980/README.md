# Symmetry 4339980 Final Proof

This lifecycle directory is the author-proofreading source of truth for manuscript
`symmetry-4339980`. It is intentionally separate from the accepted Round 2 package.

- `original/`: immutable files downloaded from SuSy on 2026-07-10.
- `source/`: editable copy of the MDPI production source.
- `evidence/`: query ledger, manifests, build logs, rendered-page checks, and SuSy readback.
- `submission_ready/`: the five current upload artifacts plus the byte-identical standalone MP4; the superseded Round 2 `coverletter.v3.pdf` is retained only for provenance. The live Cover Letter is `coverletter-final-proof.pdf`.

The final author confirmations and final SuSy `Submit` action are human-gated.

Current author-side state is `CONDITIONAL-GO`: the final source builds to 28
pages, all strict local and second-stage upload gates pass, and the code repository is
publicly accessible. MDPI production metadata and the author's final
confirmation remain external/human gates.

The proof reply contract is aligned with project 007: every production `%MDPI`
query and editor highlight is retained, every query has a following `%Author:`
reply, and the verified Qi Zhang ORCID is `0009-0008-9432-7018`.

SuSy's Supplementary uploader rejects `.mp4` through its current front-end
allowlist. The web upload therefore uses an uncompressed one-file ZIP wrapper;
the inner MP4 is byte-identical to the downloaded and Round 2 video.
