# Symmetry Submission Package

This folder keeps the Round 1 resubmission package for `symmetry-4339980`.

## Current package

- `revision_round1/upload/`: only files intended for SuSy upload.
- `revision_round1/evidence/`: validation logs, manifests, previews, and source copies used to prove the upload package is sane.
- `cover_letter/`: tracked cover-letter LaTeX source; generated build byproducts are under `cover_letter/build/`.
- `_archive/20260630-round1-build-staging/`: old staging/cache outputs kept for traceability, not for upload.

## Upload rule

Use only files under `revision_round1/upload/` for the live SuSy form. Do not upload files from `_archive/`, `cover_letter/build/`, or `revision_round1/evidence/` unless explicitly auditing or rebuilding the package.
