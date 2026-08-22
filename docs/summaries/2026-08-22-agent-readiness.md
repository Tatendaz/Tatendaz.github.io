# Session: Make tatendaz.github.io agent-ready (Is Agentic audit 66/100)

**Branch:** feat/agent-readiness
**Date:** 2026-08-22

## Prompts
1. "Improve how ready https://tatendaz.github.io is for agents. Current Is Agentic score:
   66/100 (Is Agentic readiness model based on Ora audit evidence). Implement the following
   fixes in priority order (failures first, then warnings):" followed by nine audit items —
   "1. Content without JavaScript (Essential, Partial)", "2. Agent-friendly 404s (Essential,
   Partial)", "3. Markdown content negotiation (acceptmarkdown.com) (Essential, Failed)",
   "4. Agent instruction / when-to-use (Recommended, Failed)", "5. Brand name
   discoverability (Recommended, Partial)", "6. JSON-LD structured data (Recommended,
   Partial)", "7. Trust anchor pages (Recommended, Partial)", "8. Developer resource
   discoverability (Recommended, Partial)", "9. MCP server / manifest (Recommended,
   Partial)" — each with its evidence and recommended fix — and the requirements: "Inspect
   the existing codebase before changing files. Follow each published protocol or file
   format exactly. Preserve existing product behavior and visual design. Add or update tests
   for every behavior you change. Verify every public endpoint and machine-readable file
   after implementation. Finish with a concise change summary, verification results, and any
   remaining recommendations that require product decisions or credentials."

## Steps taken
- Read the repo (single `index.html`, `sitemap.xml`, `robots.txt`, docs conventions, the
  two workflows) and the Pages config (`master` / `/`, no custom 404).
- Probed the live site: H1 present but outside `<main>`; `<main>` text measured 1812 chars
  against the audit's 1845, which identified the scanner's `<main>` scoping. Confirmed
  `.md` files serve as `text/markdown`, `.txt` as `text/plain`, `Accept: text/markdown`
  returns HTML with `Vary: Accept-Encoding`, and unknown paths return GitHub's generic 404.
- Ran a background research agent on the specs: acceptmarkdown.com (negotiation on the
  canonical URL is the only compliant form; `rel="alternate"` is a discovery aid), llmstxt.org
  (file grammar, `index.md` twins, `rel="alternate"`/`rel="describedby"` links), MCP (no
  official `.well-known`; server cards are a draft SEP), GitHub Pages (custom `404.html`
  returns 404 with its own body and no CSP; no custom headers), Is Agentic (Vercel tool, Ora
  scans, per-check methodology unpublished).
- Branched `feat/agent-readiness` from `origin/master` (the previous branch was already
  merged as PR #6; master had moved on with PR #7).
- Patched `index.html` with a one-shot script (hero into `<main>`, CSS to
  `assets/site.css`, new JSON-LD, head links, footer links). Generated `about/`, `contact/`,
  `privacy/` and `404.html` from the homepage chrome; wrote the Markdown twins, `llms.txt`,
  sitemap and robots updates, README, Makefile, tests and the CI workflow by hand.
- Verified every external link used on the new pages returns 200 (GitHub docs data-collection
  anchor, GitHub privacy statement, Google Fonts FAQ, SECURITY.md, repos).
- `make test`: 22 static checks pass, 6 live checks skipped (they run after deploy).
  Ran the live suite against the current deployment on purpose: it fails exactly on the
  things this PR adds, which shows the harness works.
- Served the branch locally and screenshotted the homepage, footer, About, Contact and 404
  pages in Chrome to confirm the design is unchanged and the new pages match it.

## Decisions
- **Fix the H1 by moving the hero into `<main>`, not by adding a second H1.** The audit's
  numbers matched `<main>`-only extraction; the restructure changes no pixels.
- **One shared stylesheet instead of four inline copies.** The homepage keeps its inline
  theme-init script (no flash); the CSS moved unchanged to `assets/site.css`.
- **Markdown twins + `rel="alternate"`/`rel="describedby"` as the static stand-in for
  content negotiation**, named as such in the README. True negotiation is a hosting
  decision, not a code change.
- **`llms.txt` "When to use this site" as an H2 file list**, so it is both a section the
  scanner can find and strictly valid llmstxt.org (every bullet is a link with notes).
- **No `llms-full.txt`, no `/agent.txt`, no `/.well-known/mcp`.** None is a published spec
  (llms-full is a convention; the others are scanner-specific or need a server).
- **Trust pages only state what the site already said**; no new biographical claims.
- **Tests use the standard library only** so `make test` works on a bare runner; live checks
  are a separate, opt-in job so PRs never depend on the deployed site.
