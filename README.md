# tatendaz.github.io

Personal site for Tatenda Zhou — Software & Systems Architect / SRE.
Static HTML, no build step (`.nojekyll`), served by GitHub Pages from `master`.

## Layout

- `index.html` — the homepage. All styling lives in `assets/site.css`, shared by every page.
- `about/`, `contact/`, `privacy/` — the trust pages. Each folder holds `index.html` plus an
  `index.md` twin with the same content in Markdown.
- `index.md` — Markdown twin of the homepage. Every HTML page advertises its twin with
  `<link rel="alternate" type="text/markdown" href="…/index.md">`. The twins are maintained by
  hand: when you change a page, change its twin too (`make test` checks they stay consistent).
- `404.html` — custom not-found page. GitHub Pages serves it with a real HTTP 404 for any
  unknown path; its body points agents at the home page, `sitemap.xml`, `llms.txt` and the
  trust pages.
- `llms.txt` — guide for AI agents in the [llmstxt.org](https://llmstxt.org/) format, including
  a "When to use this site" section and the list of Markdown twins.
- `sitemap.xml`, `robots.txt` — see "Sitemap maintenance" below.

## Checks

- `make test` runs `tests/` with the Python standard library (nothing to install). CI runs the
  same command on every push and pull request (`.github/workflows/site-checks.yml`).
- `make test-live` runs `tests/test_live.py` against the deployed site — status codes, content
  types, the 404 body, every sitemap URL. In GitHub, start the "Site checks" workflow by hand
  (Actions → Site checks → Run workflow) after a merge has deployed.

## What GitHub Pages cannot do

Two agent-readiness checks need server logic that a static host does not have:

- **Markdown content negotiation** (`Accept: text/markdown` → `text/markdown` response with
  `Vary: Accept`). GitHub Pages sends fixed headers and cannot vary the body on `Accept`. The
  Markdown twins plus `rel="alternate"` links are the static equivalent; true negotiation needs
  a host or CDN with edge logic in front of the site.
- **MCP server / `/.well-known/mcp` handshake.** Needs a running server (Streamable HTTP).

## Sitemap maintenance (`sitemap.xml`)

Because the file sits at the root of the host, its scope covers every URL on
tatendaz.github.io, including project pages served from other repos
(`/yapui/`, `/claude-usage/`, ...). Those repos do not need sitemaps of their own.

- **Keep the file free of XML comments.** Google Search Console rejected it with
  "Sitemap could not be read" on two separate reads (2026-07-26 and 2026-07-30)
  while it carried a comment block between the XML declaration and `<urlset>`;
  Bing parsed the same file without complaint. Maintenance notes live here instead.
- When a new project page goes live, append it by hand; the file discovers nothing
  on its own. Crawlers re-fetch it on their own schedule, so appending is enough;
  resubmitting in Search Console / Bing Webmaster Tools only prods them to look sooner.
- Only list URLs that already return 200. An entry pointing at a 404 is reported as
  an error in Search Console and costs trust in the whole file.
- Deliberately absent:
  - `/familytreeapp-legal/` — live, but held back until the content is ready to be indexed.
  - `/Tatendaz.github.io/` — byte-identical copy of the root; listing both would
    submit the same page under two URLs.
