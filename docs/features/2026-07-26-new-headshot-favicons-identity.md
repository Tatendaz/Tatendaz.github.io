# Feature: New headshot, proper favicons, and identity metadata for search

**Branch:** feat/new-headshot-favicons-identity
**Date:** 2026-07-26

## Summary
Replaces the old waterfront photo with the current headshot (the same one used on
the GitHub profile), serves real favicons at the sizes Google wants, and adds
Open Graph + JSON-LD identity markup so search engines show the right image,
site name, and social profiles.

## Motivation
Google results for the site showed the old photo in the result favicon — a wide
shot where the face is tiny, badly cropped inside Google's circular icon frame.
The site had no dedicated favicon (it pointed the icon link at the full-size
hero JPEG), no `og:image`, no site-name markup (Google labelled the site
"GitHub Pages documentation"), and no structured data tying the site to the
canonical social profiles — which also let Google's AI Overview pick the
Russian-localised LinkedIn URL over the English one.

## What changed
- `assets/avatar.jpg` — replaced with the current 460×460 headshot (also used
  by the hero image; same path, so no HTML change needed there).
- New `favicon.ico` (48×48, PNG-compressed ICO) at the site root.
- New `assets/icon-192.png` (192×192) and `assets/apple-touch-icon.png`
  (180×180, Apple's standard touch-icon size) — square, face-filling, and
  comfortably above Google's ≥48×48 favicon recommendation.
- `index.html` head: icon links for all three; `og:site_name`, `og:image`
  (+ width/height/alt), and Twitter card tags; JSON-LD `Person` + `WebSite`
  graph with `sameAs` pointing at the canonical profiles
  (github.com/Tatendaz, **www**.linkedin.com/in/tatendazhou, x.com/realtatendazhou).
- `index.html` head: `rel=canonical` → `https://tatendaz.github.io/`, so the
  `?theme=` query-parameter variants consolidate onto one URL.

## Notes
- Google refreshes favicons on its own crawl schedule — expect days (possibly
  weeks) after merge. Requesting indexing of the homepage in Search Console
  (pending setup) can prompt an earlier recrawl, but Google makes no timing
  promises.
- The `WebSite.name` markup is the documented signal for the site label that
  currently shows as "GitHub Pages documentation" — Google ultimately decides,
  but this is the lever it says it reads.
- The `sameAs` LinkedIn URL is deliberately the English `www` host, part of
  steering Google away from the stale `ru.linkedin.com` variant.
