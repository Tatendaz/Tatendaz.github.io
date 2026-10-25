# Session: Pin CI actions to commit SHAs

**Branch:** security/sweep-2026-10-25
**Date:** 2026-10-25

## Prompts
1. "You are worker sec-w4 in the 2026-10-25 security sweep. Read BRIEF.md
   and follow it exactly."
2. "Pick old, safe versions, never latest."

## Steps taken
- IOC grep, commit-author review, deploy keys, webhooks, secret names,
  branch protection, Pages source, Dependabot alerts: nothing unexpected.
- gitleaks (history + tree): no leaks. osv-scanner: no package manifests.
- actionlint, zizmor; read every inline script on the site.
- Pinned the actions; `make test` passes.

## Decisions
- Kept the same major versions the tags pointed at (checkout v5, dependency-review v4).
