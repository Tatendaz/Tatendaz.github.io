# Session: Numbered project cards instead of accent stripes

**Branch:** fix/card-accents
**Date:** 2026-10-26

## Prompts
1. "page render is a bit off but in incognito looks ok"
2. "can you remove these very AI looking add something else as accent" (screenshot of the orange top border on a project card)

## Steps taken
- Found the cause of the broken render: the browser kept the old `site.css` (served with `max-age=600`) while loading the new HTML.
- Removed the 3px accent top border on project cards and the 3px accent left border on the workshop band.
- Added a CSS counter that numbers the project cards 01–07 in the accent colour.
- Added `?v=20261026` to the stylesheet link on every page, and updated the tests.
- Ran `make test` (41 tests, OK). Checked that the new test fails on the old stylesheet. Took headless Chrome screenshots in dark and light mode.

## Decisions
- A catalogue number, not another stripe or glow, as the accent: it adds order to the list and uses colour on text only.
- The checkmark icons in the workshop list keep their 2px accent strokes. They draw a tick, not a stripe.
