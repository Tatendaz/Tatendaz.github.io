# Session: Open to work and consulting on the contact page

**Branch:** feat/open-to-work
**Date:** 2026-10-26

## Prompts
1. "B" (answer to: keep "Open to work" removed, or bring it back with consulting on the profile and the contact page)

## Steps taken
- Added a "Jobs and consulting" item, an email button and a "what to include" line to the contact page and its Markdown twin.
- Changed the homepage pill and its twin to "Open to work, workshops and talks". Updated meta descriptions and `llms.txt`.
- Added a test and checked that it fails without the content change. `make test`: OK.
- Took headless Chrome screenshots of the contact page.

## Decisions
- Name the four relocation countries, because recruiters filter on location.
- Consulting is scoped to coding-agent workflows, reliability and system design. Eval and benchmark audits stay off the site (owner decision of 2026-10-20).
