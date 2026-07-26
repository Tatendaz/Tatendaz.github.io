# Session: Fix stale profile photo and identity in Google results

**Branch:** feat/new-headshot-favicons-identity
**Date:** 2026-07-26

## Prompts
1. "Can you help me fix a few things: when I search on google my github profile
   still uses old image it should use new profile picture. I have circled it in
   green. tatendaz.github.io google result uses old profile also and it doesnt
   fit properly can you help me fix this. The AI section on google picks up my
   the ru.linkedin profile url and not this one
   https://www.linkedin.com/in/tatendazhou/ can we make it pickeup the english
   version." (with four screenshots of Google results)

## Steps taken
- Confirmed the GitHub avatar is already the new headshot (460×460 via the
  users API) — the github.com result thumbnail is just Google's stale cache,
  nothing to change repo-side.
- Found the real site problem: `assets/avatar.jpg` in this repo was still the
  old photo, used both as the hero image and as the favicon (a full-size JPEG
  linked as the icon).
- Replaced `assets/avatar.jpg` with the new headshot; generated
  `favicon.ico` (48), `assets/icon-192.png`, `assets/apple-touch-icon.png`
  (180) from it with sips + a small ICO packer.
- Added head metadata: icon links, `og:site_name`, `og:image` + dimensions,
  Twitter card, and a JSON-LD `Person`/`WebSite` graph with `sameAs` →
  English LinkedIn.
- Ran the pre-push gate (tests/coverage/docs/CodeRabbit local review), opened
  the PR, and handed the user steps for the Google refresh + LinkedIn-side
  fixes (stale Russian secondary-language profile).

## Decisions
- Kept the `assets/avatar.jpg` path for the hero instead of a new filename so
  the change stays one-file-swap simple; dedicated new-name icon files carry
  the favicon fix (new URLs get fetched fresh by crawlers).
- Used the 460×460 GitHub avatar as the source — no higher-res original was
  found on disk, and 460 covers every generated size (max 192) plus the hero
  (renders at ~412 CSS px on retina).
- No `.github/workflows/pr-gate.yml` in this repo; left CI installation as an
  offer rather than adding it unasked to a static site.
