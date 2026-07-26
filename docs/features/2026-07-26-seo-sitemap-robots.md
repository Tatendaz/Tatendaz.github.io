# Feature: Add sitemap.xml and robots.txt

**Branch:** feat/seo-sitemap-robots
**Date:** 2026-07-26

## Summary
Adds a host-root `sitemap.xml` listing every live page on tatendaz.github.io, and a
`robots.txt` that points crawlers at it. Both were missing — the site returned 404 for
each — so search engines had no index of the site beyond whatever they stumbled onto.

## Motivation
Only `/yapui/` had ever been submitted to Google Search Console. The root page and
`/claude-usage/` were both live and unsubmitted. Without a
sitemap, getting them indexed means submitting each URL by hand in both Google Search
Console and Bing Webmaster Tools, one at a time, and repeating that for every new page.
With one, a single sitemap submission per tool covers the whole site. New pages still
have to be appended to `sitemap.xml` by hand — a static file discovers nothing on its
own — but crawlers re-fetch the sitemap on their own schedule, so adding a URL to the
file is enough; resubmitting only prods them to look sooner.

## What changed
- `sitemap.xml` — 6 URLs (the root, `/yapui/`, `/claude-usage/`, `/Vergance/`,
  `/promptups/`, `/langchain-fde-curriculum/`) with real `lastmod` dates taken from each
  page's last source commit, plus `changefreq` and `priority`. Every entry was confirmed
  to return 200 before being listed. The header comment records which live pages are
  deliberately excluded and why, so the shorter-than-expected list doesn't read as an
  oversight.
- `robots.txt` — `Allow: /` for all agents, a `Sitemap:` line, and `Disallow` rules for
  the per-project dev-docs folders (`/*/features/`, `/*/summaries/`, `/*/sessions/`).

## Why the Disallow rules
Project pages publish the whole `docs/` folder, which on these repos also holds the
internal feature and session docs. They are served raw and reachable today —
`https://tatendaz.github.io/yapui/summaries/2026-07-02-yapui-skill.md` returns `200`.
Directory listings 404, so discovery is unlikely, but once crawling picks up there's no
reason for session logs and feature notes to compete with the landing pages in search
results. Everything there is already public on github.com, so this is search hygiene
rather than access control — if any of it were actually sensitive, robots.txt would be
the wrong tool.

## Notes
- **Scope:** because the sitemap sits at the host root, it legitimately covers project
  pages served out of *other* repos (`/yapui/` from `yapui`, `/claude-usage/` from
  `claude-usage`). Those repos don't need their own sitemaps — keeping one list here
  avoids four places to update.
- **`/familytreeapp-legal/` is live but excluded on purpose.** The content isn't ready to
  be indexed. Nothing blocks it from crawling — it's simply not advertised — so it can be
  added in one commit whenever that changes.
- **`/Tatendaz.github.io/` is excluded as a duplicate.** The portfolio repo also serves
  itself at that sub-path, byte-identical to the root (verified: same content hash), so
  the homepage exists at two URLs. Listing both would submit one page twice. No further
  fix is needed: the duplicate serves the root's `<link rel="canonical">` pointing at
  `https://tatendaz.github.io/`, so search engines consolidate on the root whichever they
  find first. Note a `robots.txt` `Disallow` would be the *wrong* tool here — a page
  crawlers are forbidden to fetch is a page whose canonical they never read.
- **The three project pages went live in this same session.** Pages was enabled on
  `Vergance`, `promptups` and `langchain-fde-curriculum` (`main` / `/docs`); all three
  built without error and now return 200, so they were added here. Merging a landing-page
  PR does not publish anything on its own — enabling Pages is the separate step.
