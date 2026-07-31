# tatendaz.github.io

Personal landing page for Tatenda Zhou — Software & Systems Architect / SRE.
Static single-page site (no build step; `.nojekyll`). Edit `index.html`.

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
