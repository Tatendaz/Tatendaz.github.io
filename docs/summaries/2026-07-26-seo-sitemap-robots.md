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
- **Third round: enabled Pages on the three repos** (`main` / `/docs`) via
  `POST /repos/Tatendaz/<repo>/pages`, polled until all three built without error and
  returned 200, then checked each served page for its title, canonical and both `ld+json`
  blocks. Added the three URLs here and re-verified all six entries return 200.
- Checked whether the root page needed a `rel=canonical` for the duplicate sub-path. It
  already has one — plus `og:image`, `twitter:card`, `og:url` and JSON-LD, all added by
  site PR #4 after this branch was cut.

## Decisions
- **One sitemap at the host root, not one per repo.** A root-level sitemap's scope
  covers the whole host, including project pages from other repos, so this is one file
  to maintain instead of four.
- **Left the not-yet-live pages out.** Landing pages for Vergance, promptups, and the
  LangChain FDE curriculum are being added in their own repos this session, but listing
  URLs that 404 would make Search Console report errors on the sitemap. They get added
  once Pages is enabled for each. Their PRs merged later the same day and that did *not*
  change it — merging a PR doesn't publish a page; enabling Pages does. Enabling it later
  in the session is what finally let them in.
- **Recorded the exclusions in the file itself, not just here.** The sitemap lists every
  deliberately-absent URL with its reason in the header comment. A short list on a host
  with more live pages than entries looks like an oversight otherwise, and the next person
  to open it would either re-add them or waste time working out why they're gone.
- **Kept `index.html` untouched.** The metadata gap that motivated leaving it alone is
  gone anyway: site PR #4 added the canonical, `og:image`, `twitter:card` and JSON-LD
  after this branch was cut. Nothing here needs to touch it.
