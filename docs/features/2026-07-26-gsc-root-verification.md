# Feature: Google Search Console verification file for the root property

**Branch:** feat/gsc-root-verification
**Date:** 2026-07-26

## Summary
Adds `googled585edcefe291ae9.html` at the site root so the URL-prefix property
`https://tatendaz.github.io/` can be verified in Google Search Console.

## Motivation
Only `/yapui/` was verified (via meta tag) until now, so Search Console had no
view of the root site: no sitemap submission, no URL Inspection, no way to
request indexing of the homepage after the favicon/identity changes in PR #4.
One root property covers every project page on the host.

## What changed
- New file `googled585edcefe291ae9.html` containing Google's standard
  verification line. Served at
  `https://tatendaz.github.io/googled585edcefe291ae9.html`.

## Notes
- The file must stay in the repo permanently: Google re-checks it periodically
  and verification lapses if it 404s.
- robots.txt (PR #3) does not block it, and `.nojekyll` means Pages serves it
  as-is.
- After merge + verify: submit `sitemap.xml` in Search Console, request
  indexing of the homepage, then import the property into Bing Webmaster Tools.
