# Feature: Add new open-source products to Selected work

**Branch:** feat/product-cards
**Date:** 2026-07-18

## Summary
Expands the Selected work section from 3 cards to 6 product cards plus a full-width
Showcase card, so the page reflects what's actually shipping in July 2026.

## Motivation
The section predated promptups, claude-usage, yapui, and herdr-launcher — the most
recent (and most shareable) public repos weren't on the site at all. The page is the
hub all social profiles point at, so it should carry the current product lineup.

## What changed
- Added cards: promptups, claude-usage, yapui, herdr-launcher (linking to their repos).
- Kept cards: Vergance, LangChain FDE.
- Moved the showcase repo card to a new full-width `work wide` variant at the bottom
  of the grid, relabelled "Private work, written up".
- New CSS: `.work.wide` (grid-column span, flex row, wrap on narrow screens).

## Notes
- Card copy reuses each repo's GitHub description almost verbatim.
- Forks (claudedirectory, loop-engineering, skills, deepsec) intentionally excluded.
- Verified with headless-Chrome renders at 1280px and 390px; the right-edge
  clipping seen at 390px reproduces identically on the live site, so it is
  pre-existing and not introduced by this change (worth a separate look).
