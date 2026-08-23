"""Checks against the deployed site. Skipped unless LIVE_SITE_URL is set.

    LIVE_SITE_URL=https://tatendaz.github.io python3 -m unittest tests.test_live -v

These are the checks an agent-readiness audit runs over HTTP: real status
codes, the right content types, a 404 body that points onward, and a
sitemap whose every URL resolves.
"""
from __future__ import annotations

import os
import re
import unittest
import urllib.error
import urllib.request

BASE = os.environ.get("LIVE_SITE_URL", "").rstrip("/")
UA = "tatendaz-site-checks/1.0 (+https://github.com/Tatendaz/Tatendaz.github.io)"
MISSING_PATH = "/some-path-that-does-not-exist"


def fetch(path: str, accept: str | None = None) -> tuple[int, str, str]:
    """GET BASE+path -> (status, content-type, body). Follows redirects."""
    headers = {"User-Agent": UA}
    if accept:
        headers["Accept"] = accept
    req = urllib.request.Request(BASE + path, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status, resp.headers.get("Content-Type", ""), resp.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as err:
        return err.code, err.headers.get("Content-Type", ""), err.read().decode("utf-8", "replace")


@unittest.skipUnless(BASE, "set LIVE_SITE_URL to run live checks")
class LiveSiteTests(unittest.TestCase):
    def test_html_pages_serve_200_with_h1(self):
        for path in ("/", "/about/", "/contact/", "/privacy/"):
            with self.subTest(path=path):
                status, ctype, body = fetch(path)
                self.assertEqual(status, 200)
                self.assertTrue(ctype.startswith("text/html"), ctype)
                self.assertIn("<h1", body)
                self.assertIn('type="text/markdown"', body)

    def test_unknown_path_returns_404_with_pointers(self):
        status, ctype, body = fetch(MISSING_PATH)
        self.assertEqual(status, 404)
        self.assertTrue(ctype.startswith("text/html"), ctype)
        for pointer in ("sitemap.xml", "llms.txt", "Page not found"):
            self.assertIn(pointer, body)
        # Markdown guidance block for agents (see test_site.NotFoundPageTests).
        for md_line in ("# 404", "- [Site map](https://tatendaz.github.io/sitemap.xml)", "- [llms.txt](https://tatendaz.github.io/llms.txt)"):
            self.assertIn(md_line, body)

    def test_llms_txt_is_plain_text(self):
        status, ctype, body = fetch("/llms.txt")
        self.assertEqual(status, 200)
        self.assertTrue(ctype.startswith("text/plain"), ctype)
        self.assertTrue(body.startswith("# "))
        self.assertIn("## When to use this site", body)

    def test_markdown_twins_serve_text_markdown(self):
        for path in ("/index.md", "/about/index.md", "/contact/index.md", "/privacy/index.md"):
            with self.subTest(path=path):
                status, ctype, body = fetch(path, accept="text/markdown")
                self.assertEqual(status, 200)
                self.assertTrue(ctype.startswith("text/markdown"), ctype)
                self.assertTrue(body.startswith("# "))

    def test_sitemap_and_robots(self):
        status, ctype, body = fetch("/sitemap.xml")
        self.assertEqual(status, 200)
        self.assertIn("xml", ctype)
        locs = re.findall(r"<loc>(.*?)</loc>", body)
        self.assertGreaterEqual(len(locs), 9)
        for loc in locs:
            with self.subTest(loc=loc):
                self.assertTrue(loc.startswith(BASE + "/"))
                self.assertEqual(fetch(loc[len(BASE):])[0], 200)
        status, ctype, body = fetch("/robots.txt")
        self.assertEqual(status, 200)
        self.assertTrue(ctype.startswith("text/plain"), ctype)
        self.assertIn("Sitemap:", body)

    def test_custom_404_page_has_its_stylesheet(self):
        status, _, body = fetch("/404.html")
        # The file itself is served as a normal page ...
        self.assertEqual(status, 200)
        self.assertIn('href="/assets/site.css"', body)
        # ... and the stylesheet it relies on is reachable.
        self.assertEqual(fetch("/assets/site.css")[0], 200)


if __name__ == "__main__":
    unittest.main()
