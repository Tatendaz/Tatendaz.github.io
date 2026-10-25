# Session: Agent-tool projects, follow buttons and workshops on the main site

**Branch:** feat/projects-and-workshops
**Date:** 2026-10-25

## Prompts
1. Team lead brief: "Update the owner's personal site ... Add a clear projects section linking
   each of the 7 project pages (and each repo). Put reliability / agent tooling first ...
   Update the hero/positioning and CTAs ... Add a short workshop section and a short
   speaking/podcast line ... Add the 7 pages to sitemap.xml and llms.txt, and update the
   Markdown twins ... Update tests ... Light AND dark mode must both work. Mobile width must
   work." Defaults given: no workshop prices; no claim of past talks.

## Steps taken
- Read the positioning and contact memories, `~/Projects/boardy/workshop/workshop.md`, each
  repo's GitHub description and each live project page's title and meta description, and
  openai/codex#53166 to check the 304 / 14 numbers.
- Rewrote `index.html`, `index.md`, `about/`, `contact/`, `llms.txt`, `sitemap.xml`, the
  shared nav and footer on every page, and the 404 project list. Added CSS for the new blocks.
- Checked the page in Chrome at 1280px and 390px, light and dark; fixed the mobile nav gutter.
- Added `ProjectLinkTests` and `PositioningTests`; ran them against `master`'s files first to
  see them fail for the right reasons, then `make test` green.

## Decisions
- Kept the existing visual language (Space Grotesk, Inter, JetBrains Mono, rust accent on
  warm paper / charcoal); the redesign is content and layout, not a new look.
- Project cards hold two links (project page, source) instead of one card-wide link, so the
  card is an `<article>`, not an `<a>`.
- The evals finding is shown as proof of method with a link to the issue, not as a service.
