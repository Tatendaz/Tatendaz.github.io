# Feature: Open to work and consulting on the contact page

**Branch:** feat/open-to-work
**Date:** 2026-10-26

## Summary
The contact page lists jobs and consulting next to workshops, podcasts and talks, with its own
email button. The homepage pill reads "Open to work, workshops and talks".

## Motivation
The 2026-10-25 update removed every job and consulting offer. Most of the owner's relocation
routes (UK, Netherlands, Ireland, Portugal Tech Visa) need a job offer, so recruiters must see
that the owner is open to work. Owner decision of 2026-10-26 (option B).

## What changed
- `contact/index.html`, `contact/index.md`: "Jobs and consulting" item (architect, SRE or AI
  engineer roles, remote or relocation to the Netherlands, the UK, Ireland or Portugal;
  consulting on coding-agent workflows, reliability and system design), a "Job or consulting"
  email button, and a line on what to include. Meta descriptions mention jobs and consulting.
- `index.html`, `index.md`: hero pill and twin line say "Open to work".
- `llms.txt`: the summary mentions roles and consulting.
- `tests/test_site.py`: `test_contact_page_lists_jobs_and_consulting`.

## Notes
No prices. The workshop stays the main paid offer on the homepage.
