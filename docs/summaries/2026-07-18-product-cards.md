# Session: Add new products to tatendaz.github.io

**Branch:** feat/product-cards
**Date:** 2026-07-18

## Prompts
1. "Can you update https://tatendaz.github.io/ with the new products I have made and
   are working on that are public like promptups claude_usage and any new repos not
   yet listed. If there are no github pages for it make them and let me know if
   anything can be done to improve visibility or to increase stars on repos and usage."

## Steps taken
- Inventoried all Tatendaz repos via `gh repo list` (public, non-fork, active).
- Confirmed the Pages site exists (master branch, `.nojekyll`, legacy build) and
  fetched the live page to diff against the repo lineup.
- Cloned the repo to ~/Projects/Tatendaz.github.io, branched `feat/product-cards`.
- Rewrote the `#work` grid: added promptups, claude-usage, yapui, herdr-launcher;
  kept Vergance + LangChain FDE; moved Showcase to a full-width bottom card with a
  small `.work.wide` CSS addition.
- Verified with headless-Chrome screenshots (desktop + mobile) against the live site.
- Ran the pre-push gate (no test runner in a static site; coverage check ok) and a
  local CodeRabbit review before pushing.

## Decisions
- Cards link to GitHub repos (not project microsites) so traffic lands where stars
  accrue; yapui's own Pages site is reachable from its repo.
- Excluded forks and pre-2023 course repos from the lineup.
- Showcase kept on the page but as the wide closing card — it fronts the private
  Quant_Backtest_Platform / familytreeapp work, which stays the consulting hook.
