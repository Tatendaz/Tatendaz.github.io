# Feature: Numbered project cards instead of accent stripes

**Branch:** fix/card-accents
**Date:** 2026-10-26

## Summary
The project cards lose their 3px orange top border and the workshop box loses its 3px orange
left border. Each project card now starts with a small orange catalogue number, 01 to 07. The
stylesheet link carries a version tag so browsers fetch the new file after a change.

## Motivation
The owner said the thick accent stripes look AI-generated. After the 2026-10-25 update the
owner's browser also showed the new HTML with the old cached stylesheet, so the cards rendered
unstyled until a hard refresh.

## What changed
- `assets/site.css`: no `border-top` on `.projgrid.three .proj`, no `border-left` on `.band`.
  A CSS counter on `#projects` prints `01`–`07` before each card's label, with empty alt text
  so screen readers skip it.
- `index.html`, `404.html`, `about/`, `contact/`, `privacy/`: link `/assets/site.css?v=20261026`.
- `tests/test_site.py`: `STYLESHEET_LINK` constant; a test that the stylesheet has no 3px+
  accent stripe and has the card counter. `tests/test_live.py`: expects a versioned link.

## Notes
Bump the `?v=` value in all five pages and in `STYLESHEET_LINK` whenever `assets/site.css`
changes.
