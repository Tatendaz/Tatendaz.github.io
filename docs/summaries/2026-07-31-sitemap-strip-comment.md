# Session: Strip the XML comment from sitemap.xml

**Branch:** fix/sitemap-strip-comment
**Date:** 2026-07-31

## Prompts
1. "any luck?" — asking whether the GSC sitemap status had recovered after the
   2026-07-30 resubmission.
2. "do b" — approving option B: request indexing individually in GSC for the
   four pages the unparsed sitemap had left undiscovered (/claude-usage/,
   /Vergance/, /promptups/, /langchain-fde-curriculum/).
3. "Do A after" — approving option A: this PR, which strips the XML comment
   suspected of breaking Google's sitemap parser.

## Steps taken
- Scheduled check found the resubmitted sitemap rejected again: drilldown showed
  "Last read 7/30/26", "Sitemap could not be read", 0 discovered — a fresh read,
  so not a stale-status artifact.
- Re-validated the served file: HTTP 200, `content-type: application/xml`, no
  BOM, `xmllint` clean, 6 URLs; Bing parses it to Success/6. Concluded the
  comment block between the declaration and `<urlset>` is the prime suspect.
- Requested indexing for the four undiscovered pages via URL Inspection (all
  confirmed "Indexing requested"; the fourth needed one retry after a transient
  "problem submitting your indexing request" error).
- This PR: removed the comment from `sitemap.xml`, moved its content to a
  "Sitemap maintenance" section in `README.md`, added these docs entries.

## Decisions
- Preserve the comment's content in `README.md` rather than delete it: the
  exclusion rationale (familytreeapp-legal held back deliberately;
  /Tatendaz.github.io/ is a root duplicate) prevents well-meaning "fixes".
- Keep the six `<url>` entries byte-identical so the diff isolates the comment
  removal — if GSC accepts the file now, the cause is unambiguous.
- Interim indexing requests (option B) went first so launch-week pages queue for
  crawl regardless of how the sitemap experiment turns out.
