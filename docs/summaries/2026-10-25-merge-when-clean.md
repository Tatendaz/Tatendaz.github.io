# Session: Merge-when-clean job; Dependabot PRs get CodeRabbit reviews again

**Branch:** security/hardening-2-2026-10-25
**Date:** 2026-10-25

## Prompts
1. "HARDENING.md changed: add the auto-merge job from
   templates/merge-when-clean.yml to every repo you harden. Do NOT add
   dependabot[bot] to CodeRabbit ignore lists; remove it if you already did."

## Steps taken
- Copied the template unchanged; deleted `.coderabbit.yaml`.
- `actionlint` and `zizmor` on the workflows: clean.

## Decisions
- Deleted the whole `.coderabbit.yaml` instead of leaving `inheritance: true`
  alone in it: with no repo file, the web UI settings apply as before #14.
