# Feature: Pin CI actions to commit SHAs

**Branch:** security/sweep-2026-10-25
**Date:** 2026-10-25

## Summary
`site-checks.yml` and `dependency-review.yml` now pin `actions/checkout` and
`actions/dependency-review-action` to full commit SHAs, and checkout no
longer leaves the job token in `.git/config`.

## Motivation
A tag can be moved to new code at any time; a SHA cannot. Supply-chain worms
in 2026 spread by retagging actions and packages. `zizmor` rated the tags
high and the persisted credentials medium. The rest of the 2026-10-25
security sweep found nothing to fix: the site is static, its only scripts
set the colour theme, and it loads no third-party script.

## What changed
- `actions/checkout@v5` -> `@fbc6f39... # v5.1.0`, with `persist-credentials: false`
- `actions/dependency-review-action@v4` -> `@2031cfc... # v4.9.0`

## Notes
No change to the site itself.
