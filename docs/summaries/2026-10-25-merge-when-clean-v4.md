# Session: merge-when-clean template v6

**Branch:** security/merge-when-clean-v4
**Date:** 2026-10-25

## Prompts
1. "templates/merge-when-clean.yml is now v4. Repos already merged with v2/v3:
   open one small follow-up PR to v4 when your other work is done."
2. "templates/merge-when-clean.yml is now v5 ... Replace any v4 copy with v5."
3. "templates/merge-when-clean.yml is now v6 ... Use v6 wherever you were about
   to put v5. No more template changes are planned."

## Steps taken
- Copied v4 (`f0c005a3…`), then v5 (`1c493dd7…`), then v6 (`af7e7bd9…`),
  each unchanged after checking its sha256. The branch name still says v4.
- `actionlint` and `zizmor` after each copy: clean. `make test`: OK.

## Decisions
- No hold-paths file: nothing in this repo runs with a secret.
