# Session: Verify the root site in Google Search Console

**Branch:** feat/gsc-root-verification
**Date:** 2026-07-26

## Prompts
1. "tatendaz.github.io in Search Console and submitting the sitemap  what do I
   need to do?"

## Steps taken
- Checked live state: `sitemap.xml` and `robots.txt` still 404 because PR #3
  is unmerged; asked Tatenda to merge it.
- Started the Search Console "Add property" flow in Chrome (URL-prefix
  `https://tatendaz.github.io/`); Google issued the HTML-file verification
  token `googled585edcefe291ae9.html`.
- Created this branch with the verification file at the repo root plus these
  docs entries, ran the pre-push gate, and opened the PR.
- Next (after merge + Pages deploy): click Verify in Search Console, submit
  the sitemap, request indexing of the homepage, import into Bing.

## Decisions
- HTML-file method over meta tag: keeps `index.html` untouched and the token
  is trivially auditable in the repo root.
- File content written from Google's documented standard format
  (`google-site-verification: <filename>`) rather than downloading the file
  through the browser.
