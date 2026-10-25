# Feature: merge-when-clean template v5

**Branch:** security/merge-when-clean-v4
**Date:** 2026-10-25

## Summary
Replaces the v2 copy of `merge-when-clean.yml` with the owner's template v5.

## Motivation
v3 to v5 fix gaps found by reviews during the 2026-10-25 security sweep:
an optional `.github/merge-hold-paths` file (read from the default branch;
a bad regex means merge nothing), any reviewer's latest "changes requested"
review now blocks, and no `tr | grep -q` pipes that could turn a match into a
pass under `pipefail`.

## What changed
- `.github/workflows/merge-when-clean.yml`: template v5 (sha256 `1c493dd7…`), unchanged.

## Notes
No `.github/merge-hold-paths` here: the site has no job that holds secrets.
