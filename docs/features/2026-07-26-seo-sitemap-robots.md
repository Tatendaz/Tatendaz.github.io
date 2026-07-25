# Feature: Add sitemap.xml and robots.txt

**Branch:** feat/seo-sitemap-robots
**Date:** 2026-07-26

## Summary
Adds a host-root `sitemap.xml` listing every live page on tatendaz.github.io, and a
`robots.txt` that points crawlers at it. Both were missing — the site returned 404 for
each — so search engines had no index of the site beyond whatever they stumbled onto.

## Motivation
Only `/yapui/` had ever been submitted to Google Search Console. The root page,
`/claude-usage/`, and `/familytreeapp-legal/` were all live and unsubmitted. Without a
sitemap, getting them indexed means submitting each URL by hand in both Google Search
Console and Bing Webmaster Tools, one at a time, and repeating that for every new page.
With one, a single sitemap submission per tool covers the whole site and picks up
additions automatically.

## What changed
- `sitemap.xml` — the 4 live URLs with real `lastmod` dates taken from each page's last
  source commit, plus `changefreq` and `priority`.
- `robots.txt` — `Allow: /` for all agents and a `Sitemap:` line.

## Notes
- **Scope:** because the sitemap sits at the host root, it legitimately covers project
  pages served out of *other* repos (`/yapui/` from `yapui`, `/claude-usage/` from
  `claude-usage`). Those repos don't need their own sitemaps — keeping one list here
  avoids four places to update.
- **Follow-up:** landing pages for `Vergance`, `promptups`, and `langchain-fde-curriculum`
  are in flight in their own repos. Once Pages is enabled for each, add their URLs here
  and resubmit.
- The root `index.html` still has no `<link rel="canonical">`, no `og:image`, and no
  Twitter card tags — worth a separate pass, out of scope here.
