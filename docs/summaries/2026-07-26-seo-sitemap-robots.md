# Session: Get every page submittable to Google and Bing

**Branch:** feat/seo-sitemap-robots
**Date:** 2026-07-26

## Prompts
1. "can you remind me to submit all pages to google seo vergence, claude-usage and my
   own github page. yapui is already submitted."
2. "and any page I may have forgotten in my github pages"
3. "submit to bing as well"
4. "promptups and langchain fde curricilum?"
5. "do both"
6. "Vergance, promptups, langchain-fde-curriculum . Later today I will do the demo gif"
7. "remove from pr 3 https://tatendaz.github.io/familytreeapp-legal/ its not yet ready.
   Does this PR include vergance promptups langchain-fde-curriculum claude-usage?
   basically check that it covers repos on tatendaz.github.io"
8. "pr 11 4 and 5 are merged"

## Steps taken
- Enumerated every Pages site across the account with `gh api .../pages` and confirmed
  each with a live HTTP check. Found four live pages, not three: the root,
  `/yapui/`, `/claude-usage/`, and `/familytreeapp-legal/` — the last of which had been
  forgotten entirely.
- Confirmed `sitemap.xml` and `robots.txt` both 404'd at the root.
- Pulled real `lastmod` dates from each page's most recent source commit rather than
  stamping everything with today's date.
- Wrote `sitemap.xml` + `robots.txt`.
- **Second round, after the three landing-page PRs merged.** Re-enumerated every public
  repo's Pages status and HTTP code to answer "does this cover everything on the host".
  Result: `claude-usage` is covered; `Vergance`, `promptups` and `langchain-fde-curriculum`
  are **not**, because Pages is still off on all three (`/pages` 404s, URLs 404). Also
  surfaced `/Tatendaz.github.io/`, which serves a byte-identical copy of the root.
- Removed `/familytreeapp-legal/` on request — live, but not ready to be indexed.

## Decisions
- **One sitemap at the host root, not one per repo.** A root-level sitemap's scope
  covers the whole host, including project pages from other repos, so this is one file
  to maintain instead of four.
- **Left the not-yet-live pages out.** Landing pages for Vergance, promptups, and the
  LangChain FDE curriculum are being added in their own repos this session, but listing
  URLs that 404 would make Search Console report errors on the sitemap. They get added
  once Pages is enabled for each. Their PRs merged later the same day and this still
  holds — merging the PR doesn't publish the page; enabling Pages does.
- **Recorded the exclusions in the file itself, not just here.** The sitemap now lists
  every deliberately-absent URL with its reason in the header comment. A three-entry
  sitemap on a host with five live pages looks like an oversight otherwise, and the next
  person to open it would either re-add them or waste time working out why they're gone.
- **Kept `index.html` untouched.** It's missing a canonical link, `og:image`, and
  Twitter card tags, but that's a separate change and doesn't block submission.
