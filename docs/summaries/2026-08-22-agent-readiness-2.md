# Session: Rescan follow-up — hero as a div, Codex and Grok reviews

**Branch:** feat/agent-readiness-2
**Date:** 2026-08-22

## Prompts
1. "merged https://github.com/Tatendaz/Tatendaz.github.io/pull/8"
2. "Improve how ready https://tatendaz.github.io is for agents. Current Is Agentic score:
   72/100 …" — the rescan's six remaining items (content without JavaScript, agent-friendly
   404s, Markdown content negotiation, brand name discoverability, developer resource
   discoverability, MCP server / manifest) with the same requirements as the first round,
   plus: "ask codex cli to also check your pr and grok cli".

## Steps taken
- Verified the deployed site after the merge: `make test-live` 6/6, real 404 with pointers,
  `/about` → `/about/`, Markdown twins as `text/markdown`, 2,154 chars inside `<main>`, H1
  inside `<main>`, JSON-LD `Person` + `WebSite`. Found that project-site 404s
  (`/yapui/missing`) do not fall back to the root `404.html`.
- Read the rescan: Recommended checks went from 3/9 to 7/10 (JSON-LD, trust pages, agent
  instruction file now pass); the two Essential partials repeat the pre-deploy evidence
  verbatim. Reasoned that either the scanner cached the fetch or it strips `<header>`.
- Renamed the hero element to `<div class="hero">` on the homepage and on the five project
  pages (CSS selector rename there), added the "no boilerplate element inside `<main>`" test
  everywhere, re-ran all suites, pushed.
- Triggered a rescan from the Is Agentic page and watched the API for a newer `scanned_at`.
- Ran `codex review` and `grok -p` over the PR diffs; triaged their findings like
  CodeRabbit's.

## Decisions
- Fix the `<header>` possibility rather than wait for the cache theory to be proven: the
  change is invisible and the test guards it.
- Keep the 404 as HTML: GitHub Pages cannot serve a `text/markdown` 404, and the body already
  names the sitemap, llms.txt, the trust pages and the project docs.
- Items 3–6 of the rescan stay product decisions (hosting with edge logic, an MCP server, an
  API, off-site brand signals); none is a code change on a static GitHub Pages site.
