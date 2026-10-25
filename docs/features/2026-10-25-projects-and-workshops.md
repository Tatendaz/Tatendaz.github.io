# Feature: Agent-tool projects, follow buttons and workshops on the main site

**Branch:** feat/projects-and-workshops
**Date:** 2026-10-25

## Summary
The homepage now links the seven agent-tool project pages built on 2026-10-19, leads with
Follow on X / Follow on LinkedIn buttons, and offers a coding-agent workshop for engineering
teams plus podcasts and talks. Web3 and the consulting / executive-workshop pitch are gone.

## Motivation
The project pages were live but nothing on tatendaz.github.io linked to them; the owner could
not find them. A Dataconomy article may send editors and readers here, and the owner's goal for
that traffic is follows on X and LinkedIn first, workshops second (decision of 2026-10-20).

## What changed
- `index.html`: new hero copy and Follow buttons; `#projects` with the seven project pages and
  their repos, review and QA tools first (coderabbit-failover, CodeAndConfirm, T-mods), then
  QuotaSignal, Model Picker, Mission Control, herdr-launcher; a short `#evidence` note on
  openai/codex#53166 (304 runs, 14 searched or read outside the workspace); `#workshops` ("From chat to
  coding agent", flat fee per team, no prices); `#talks`; older projects in `#work`; footer
  with Follow buttons. JSON-LD Person and WebSite descriptions updated, Web3 removed.
- `about/`, `contact/` (HTML and Markdown twins): same positioning; the contact page lists
  workshops, podcasts and talks only.
- Shared nav on every page: Projects, Workshops, Talks, Follow. Shared footer: Follow buttons.
- `404.html`: links the seven agent-tool pages.
- `index.md`, `llms.txt`, `sitemap.xml`: list the seven pages.
- `assets/site.css`: project cards, evidence note, workshop list, talks row, "More projects"
  list; mobile nav now keeps its 28px side gutter (the old rule zeroed it).
- `tests/test_site.py`: `ProjectLinkTests` and `PositioningTests` (every project page on the
  homepage in order, in the twins, About, llms.txt and sitemap; Follow buttons lead the hero;
  workshop and talks sections carry their mailto; no Web3, prices, newsletter, "OpenAI
  confirmed", or em/en dashes in public files). `tests/test_live.py`: the live homepage links
  every agent-tool page and each returns 200.

## Notes
- Copy for each project comes from its GitHub description and its live page's meta
  description; no new numbers.
- No workshop prices on the site (owner has not set them).
- Speaking record, from the owner on 2026-10-25: guest on the Koshelek Team podcast
  (YouTube, in Russian) and former club president of a Toastmasters club in Saint
  Petersburg. No club name or dates, because the owner gave none.
- Consulting and fractional / advisory work no longer appear anywhere. Put a line back on
  `/contact/` if the owner still wants those enquiries.
