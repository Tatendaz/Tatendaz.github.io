# Feature: Merge-when-clean job; Dependabot PRs get CodeRabbit reviews again

**Branch:** security/hardening-2-2026-10-25
**Date:** 2026-10-25

## Summary
Adds the owner's `merge-when-clean.yml` workflow and removes the
`.coderabbit.yaml` that #14 added.

## Motivation
Owner decision 2026-10-25: no PR should sit stuck. The job merges Dependabot
PRs and the owner's `security/*` or `automerge` PRs once CI is green, a real
review ran (CodeRabbit "Review completed" or `review-failover` success) and
0 threads are open. That needs CodeRabbit to auto-review Dependabot PRs, so
the `ignore_usernames: ["dependabot[bot]"]` setting from #14 is gone. It was
the file's only purpose.

## What changed
- `.github/workflows/merge-when-clean.yml` (new): the template, unchanged.
- `.coderabbit.yaml`: deleted.

## Notes
The site deploys through GitHub Pages' own branch build, not a workflow in
this repo, so there is no deploy workflow to give a `workflow_dispatch`.
