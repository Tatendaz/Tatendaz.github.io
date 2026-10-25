# Session: merge-when-clean template v6

**Branch:** security/merge-when-clean-v4
**Date:** 2026-10-25

## Prompts
1. "templates/merge-when-clean.yml is now v4. Repos already merged with v2/v3:
   open one small follow-up PR to v4 when your other work is done."

## Steps taken
- Checked the template hash (`f0c005a3…`), copied it unchanged.
- `actionlint` and `zizmor`: clean. `make test`: OK.

## Decisions
- No hold-paths file: nothing in this repo runs with a secret.
