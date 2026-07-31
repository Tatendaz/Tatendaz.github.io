# Feature: Strip the XML comment from sitemap.xml

**Branch:** fix/sitemap-strip-comment
**Date:** 2026-07-31

## Summary
Removes the 22-line comment block that sat between the XML declaration and
`<urlset>` in `sitemap.xml`, and moves its content (maintenance rules and the
list of deliberately excluded URLs) into a "Sitemap maintenance" section in
`README.md`. The sitemap's six `<url>` entries are unchanged.

## Motivation
Google Search Console rejected the sitemap with "Sitemap could not be read"
(0 pages discovered) on two separate reads: the original submission on
2026-07-26 and a manual resubmission on 2026-07-30. The file is otherwise
provably clean — it serves HTTP 200 with `content-type: application/xml`, has
no BOM, passes `xmllint`, and Bing Webmaster Tools parsed the identical file to
"Success / 6 URLs discovered" on the day it was submitted. The comment block is
the file's only non-standard feature, and Google's sitemap parser failing on
content before the root element is a known pattern. Removing it is the
cheapest root-cause candidate; the operational notes are preserved in README.md
where no parser can trip on them.

## What changed
- `sitemap.xml`: deleted the comment block (lines 2–23). The file now goes
  straight from `<?xml ...?>` to `<urlset ...>`. No URL entries touched.
- `README.md`: new "Sitemap maintenance" section carrying the comment's
  content, plus a warning to keep the file comment-free with the GSC rejection
  dates as evidence.

## Notes
- After merge, GitHub Pages redeploys the file automatically; the sitemap then
  needs a manual resubmission in Google Search Console to trigger a fresh read.
- Bing needs nothing: it already parses the file successfully and re-fetches on
  its own schedule.
- If GSC rejects the comment-free file again, the next lever is submitting
  `sitemap.xml?v=2` as an additional sitemap entry to bypass any cached fetch.
