# Feature: Agent readiness — H1 in `<main>`, trust pages, llms.txt, custom 404, JSON-LD, Markdown twins

**Branch:** feat/agent-readiness
**Date:** 2026-08-22

## Summary
Fixes every item of the Is Agentic audit (is-agentic.com, scans run by Ora; score 66/100
on 2026-08-22) that a static GitHub Pages host can fix. The homepage hero and H1 now sit
inside `<main>`; the JSON-LD is a top-level `Person` with `name`, `description` and `url`;
`/about/`, `/contact/` and `/privacy/` exist with 500+ characters each; `/llms.txt` follows
llmstxt.org and has a "When to use this site" section; `404.html` gives unknown paths a
short body that points agents at the home page, sitemap, llms.txt and trust pages; every
HTML page has a Markdown twin (`index.md`) advertised with `rel="alternate"
type="text/markdown"` and `rel="describedby"` links. A stdlib-only test suite (`make test`)
and a CI workflow guard all of it.

## Motivation
The audit's evidence, and what each item turned out to mean for this site:

1. **Content without JavaScript** — "Only 1845 chars of text content, no H1 tag". The page
   had an H1, but the scanner scopes to `<main>`: the hero (with the H1) sat outside it and
   `<main>` alone measured 1812 characters. Moving the hero inside `<main>` fixes both halves.
2. **Agent-friendly 404s** — GitHub already returned a real 404, with GitHub's generic page.
   A custom `404.html` keeps the 404 status and adds the "where to look next" body.
3. **Markdown content negotiation** — needs `Accept`-based responses and `Vary: Accept`.
   GitHub Pages has no server logic and no custom headers (see "Not fixable here").
4. **Agent instruction / when-to-use** — there was no `llms.txt` at all.
5. **Brand name discoverability** — mostly off-site; on-site identity signals strengthened.
6. **JSON-LD** — the Person was nested in an `@graph` and had no `description`.
7. **Trust anchor pages** — `/about/` and `/privacy/` did not exist.
8. **Developer resource discoverability** — project repos and pages were only on the
   homepage cards; they are now listed with descriptions in `llms.txt` and on `/about/`.
9. **MCP server / manifest** — needs a running server (see "Not fixable here").

## What changed
- `index.html`
  - `<header class="hero">` (pill, H1, lede, CTAs, avatar) moved inside `<main>`; the
    sections are wrapped in `<div class="wrap">` instead of `main.wrap`. Visual output is
    unchanged.
  - Inline `<style>` extracted to `assets/site.css` (byte-for-byte the same rules, plus the
    new `.page`/`.foot-links` rules) so the new pages share one stylesheet.
  - JSON-LD rewritten as two top-level blocks: `Person` (name, givenName, familyName,
    description, url, mainEntityOfPage, image, jobTitle, email, knowsAbout, sameAs) and
    `WebSite` (name, url, description, inLanguage, publisher → Person).
  - Head: `<link rel="alternate" type="text/markdown" href="/index.md">`,
    `<link rel="describedby" href="/llms.txt">`, `<meta name="author">`.
  - Footer: a small mono links row — About · Contact · Privacy · llms.txt · Sitemap.
- New pages, same chrome (nav, theme toggle, footer) as the homepage:
  - `about/index.html` — `AboutPage` JSON-LD with `mainEntity` Person; who, what, projects,
    how to work together. Content is taken from the homepage; nothing new is claimed.
  - `contact/index.html` — `ContactPage` JSON-LD; email CTAs, what Tatenda is open to, what
    to include in a message, where to report security issues.
  - `privacy/index.html` — `WebPage` JSON-LD; no cookies/analytics, GitHub Pages IP logging
    (linked to GitHub's docs), Google Fonts requests (linked to Google's FAQ), the
    `localStorage` theme key, email handling. Dated 2026-08-22.
  - `404.html` — `noindex`; short body with absolute links to `/`, `/sitemap.xml`,
    `/llms.txt`, the trust pages and the five project pages.
- Markdown twins: `index.md`, `about/index.md`, `contact/index.md`, `privacy/index.md`
  (the `index.md` convention from llmstxt.org). GitHub Pages serves them as
  `text/markdown; charset=utf-8`.
- `llms.txt` — H1, blockquote summary, a free-text paragraph, then H2 file lists:
  "When to use this site", Pages, Markdown versions, Projects and developer resources,
  Machine-readable files, Optional. Every bullet is `- [name](url): notes`.
- `sitemap.xml` — root `lastmod` bumped to 2026-08-22; `/about/`, `/contact/`, `/privacy/`
  added. Still comment-free.
- `robots.txt` — comment pointing at `/llms.txt` (no rule changes).
- `Makefile` — `make test`, `make test-live`, `make serve`.
- `tests/test_site.py` — 22 static checks (H1 inside `<main>`, text length, JSON-LD fields,
  alternates/describedby → existing twins, trust-page length and types, 404 body, llms.txt
  grammar and local-URL existence, sitemap/robots, twin sanity).
- `tests/test_live.py` — 6 HTTP checks against the deployed site, skipped unless
  `LIVE_SITE_URL` is set (status codes, content types, 404 body, every sitemap URL).
- `.github/workflows/site-checks.yml` — `make test` on push/PR; `make test-live` on
  `workflow_dispatch`.
- `README.md` — layout, checks, and the "What GitHub Pages cannot do" section.

## Not fixable here (product decisions)
- **Markdown content negotiation (`Accept: text/markdown` + `Vary: Accept`)** — acceptmarkdown.com
  defines compliance as negotiation on the canonical URL; `rel="alternate"` links are a
  discovery aid only. GitHub Pages cannot set headers or vary bodies. Options: put the site
  behind Cloudflare ("Markdown for Agents" toggle, needs a custom domain on Cloudflare DNS) or
  move to Cloudflare Workers / Netlify with an edge function.
- **MCP server / `/.well-known/mcp`** — the scanner probes a path no MCP spec defines; full
  credit needs a live Streamable HTTP server. The "first-party MCP server" it credited is
  GitHub's own, matched on the `github.io` domain.
- **Brand name search** — ranking depends on external links and listings; on-site signals
  (consistent name, JSON-LD `sameAs`, `author` meta, trust pages) are now in place.

## Notes
- After merge, GitHub Pages redeploys within a few minutes. Then run the live checks:
  `make test-live` locally, or Actions → "Site checks" → "Run workflow".
- Re-scan with `npx is-agentic tatendaz.github.io` (or https://is-agentic.com/).
- The Privacy page text was written from the site's actual behaviour; read it once to make
  sure the email-handling sentence matches what you do.
- The Markdown twins are maintained by hand; `make test` fails if a project link on the
  homepage is missing from `index.md`, or a twin referenced from a page does not exist.
