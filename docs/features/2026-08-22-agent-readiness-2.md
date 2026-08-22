# Feature: Hero as `<div class="hero">` so content extractors keep the H1

**Branch:** feat/agent-readiness-2
**Date:** 2026-08-22

## Summary
Follow-up to PR #8 after the first post-deploy Is Agentic rescan (72/100). The homepage hero
(pill, H1, lede, CTAs, avatar) was a `<header>` inside `<main>`; it is now `<div class="hero">`.
The 404 page names "docs" among its pointers. Tests now assert that no
`<header>`/`<nav>`/`<aside>`/`<footer>` sits inside `<main>` on any page.

## Motivation
The rescan repeated the old evidence for "Content without JavaScript" ("Only 1845 chars of text
content, no H1 tag") even though the deployed page has the H1 inside `<main>` and 2,150+
characters there. Two explanations fit: the scanner fetched a cached copy (it ran four minutes
after the deploy; GitHub Pages caches for 600 s), or it strips `<header>` elements as
boilerplate before counting text and looking for the H1 — in which case the hero, and the H1
with it, vanish and the remaining sections measure the same ~1,800 characters as before.
Renaming the element removes the second possibility at no visual cost; the CSS only ever
targeted `.hero`.

## What changed
- `index.html`: `<header class="hero">` → `<div class="hero">` (closing tag to match). No CSS
  change; `assets/site.css` never used a `header` selector.
- `404.html`: `llms.txt` is described as the "guide and docs index for AI agents" (the audit names
  "sitemap, llms.txt, or docs index" as the pointers it wants).
- `tests/test_site.py`: `test_no_boilerplate_elements_inside_main` checks every page including
  `404.html` for `<header>`/`<nav>`/`<aside>`/`<footer>` *elements* inside `<main>` (tag-name
  match, so prose or `<navbar>` cannot trip it); the hero assertion checks for a `div` carrying the
  `hero` class token. (Both tightened after a Grok CLI review.)
- The five project pages got the same change in their own PRs (yapui #12, claude-usage #17,
  Vergance #15, promptups #13, langchain-fde-curriculum #10): `<header>` → `<div class="hero">`
  with the single `header {…}` rule renamed to `.hero {…}`.

## Notes
- After merge: `make test-live`, then rescan at https://is-agentic.com/scan/tatendaz.github.io
  ("Rescan" under the score) at least 10 minutes after the deploy so no CDN copy is stale.
- Still not fixable on GitHub Pages: `Accept: text/markdown` negotiation with `Vary: Accept`
  (needs edge logic, e.g. Cloudflare), a live MCP handshake at `/.well-known/mcp` (needs a
  server), brand-name search ranking (off-site), and "API docs / auth docs" discoverability
  (there is no API).
