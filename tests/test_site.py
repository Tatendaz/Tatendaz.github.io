"""Static checks for the agent-readiness files of tatendaz.github.io.

Runs with the Python standard library only:  python3 -m unittest discover -s tests -v
Every check here guards a behaviour an AI agent or crawler depends on:
an H1 and real text inside <main>, valid JSON-LD, Markdown twins, a real
404 page with pointers, an llms.txt in the llmstxt.org format, and a
sitemap/robots pair that only lists files that exist.
"""
from __future__ import annotations

import html
import json
import re
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://tatendaz.github.io"

# URL path -> repo file for every HTML page served from this repository.
PAGES = {
    "/": "index.html",
    "/about/": "about/index.html",
    "/contact/": "contact/index.html",
    "/privacy/": "privacy/index.html",
}
TRUST_PAGES = ("/about/", "/contact/", "/privacy/")
# Project pages live in other repositories; only the live test can check them.
EXTERNAL_PROJECT_PATHS = {"yapui", "claude-usage", "Vergance", "promptups", "langchain-fde-curriculum"}

TAG_RE = re.compile(r"<[^>]+>")
SCRIPT_STYLE_RE = re.compile(r"<(script|style)\b[^>]*>.*?</\1>", re.S | re.I)
LINK_TAG_RE = re.compile(r"<link\b[^>]*>", re.I)
ATTR_RE = re.compile(r'([A-Za-z_:][-A-Za-z0-9_:.]*)="([^"]*)"')
LD_JSON_RE = re.compile(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', re.S)
H1_RE = re.compile(r"<h1\b[^>]*>(.*?)</h1>", re.S | re.I)
HREF_RE = re.compile(r'href="([^"]*)"')
# Elements that readability-style extractors drop as boilerplate before counting text.
# A tag name ends at whitespace, "/" or ">", so <header-card> or <nav-item> do not match.
BOILERPLATE_TAG_RE = re.compile(r"<(header|nav|aside|footer)(?=[\s/>])", re.I)
# A <div> whose class attribute (not data-class) lists "hero" as a whole token (not foo-hero).
HERO_DIV_RE = re.compile(r'<div(?=[\s/>])[^>]*\sclass="(?:[^"]*\s)?hero(?:\s[^"]*)?"', re.I)
LLMS_LINK_RE = re.compile(r"^- \[[^\]]+\]\((https?://[^)\s]+)\)(?:: .+)?$")


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def visible_text(fragment: str) -> str:
    """Text a non-JS client sees: drop script/style, strip tags, collapse whitespace."""
    no_code = SCRIPT_STYLE_RE.sub("", fragment)
    text = TAG_RE.sub(" ", no_code)
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def main_html(doc: str) -> str:
    m = re.search(r"<main\b[^>]*>(.*?)</main>", doc, re.S | re.I)
    assert m, "no <main> element"
    return m.group(1)


def head_links(doc: str) -> list[dict[str, str]]:
    return [dict(ATTR_RE.findall(tag)) for tag in LINK_TAG_RE.findall(doc)]


def ld_json_blocks(doc: str) -> list[dict]:
    return [json.loads(block) for block in LD_JSON_RE.findall(doc)]


def meta_content(doc: str, name: str) -> str | None:
    m = re.search(rf'<meta name="{re.escape(name)}" content="([^"]*)"', doc)
    return m.group(1) if m else None


def local_file_for(url_path: str) -> Path | None:
    """Map a path on tatendaz.github.io to the file in this repo that serves it."""
    first = url_path.strip("/").split("/")[0]
    if first in EXTERNAL_PROJECT_PATHS:
        return None
    rel = url_path.lstrip("/")
    if rel == "" or rel.endswith("/"):
        rel += "index.html"
    return ROOT / rel


class HomepageTests(unittest.TestCase):
    def setUp(self):
        self.doc = read("index.html")
        self.main = main_html(self.doc)

    def test_single_h1_lives_inside_main(self):
        # Readability-style extractors scope to <main>; the H1 must be in there.
        self.assertEqual(len(H1_RE.findall(self.doc)), 1)
        h1s = H1_RE.findall(self.main)
        self.assertEqual(len(h1s), 1)
        self.assertEqual(visible_text(h1s[0]), "Tatenda Zhou")

    def test_main_has_enough_text_without_javascript(self):
        text = visible_text(self.main)
        self.assertGreaterEqual(len(text), 500, "audit bar: 500+ chars of raw text in <main>")
        self.assertRegex(self.main, HERO_DIV_RE, "hero (pill, H1, lede) must be a div inside <main>")
        self.assertIn("10+ years in enterprise software", text)

    def test_jsonld_person_then_website(self):
        blocks = ld_json_blocks(self.doc)
        self.assertGreaterEqual(len(blocks), 2)
        person, website = blocks[0], blocks[1]
        self.assertEqual(person["@type"], "Person")
        for key in ("name", "description", "url", "image", "jobTitle", "sameAs", "email"):
            self.assertTrue(person.get(key), f"Person.{key} missing")
        self.assertEqual(person["name"], "Tatenda Zhou")
        self.assertGreaterEqual(len(person["description"]), 80)
        self.assertEqual(person["url"], f"{SITE}/")
        self.assertGreaterEqual(len(person["sameAs"]), 3)
        self.assertTrue(all(u.startswith("https://") for u in person["sameAs"]))
        self.assertEqual(website["@type"], "WebSite")
        self.assertEqual(website["url"], f"{SITE}/")
        self.assertTrue(website.get("name") and website.get("description"))
        self.assertEqual(website["publisher"]["@id"], person["@id"])

    def test_links_to_trust_pages_and_agent_files(self):
        hrefs = set(HREF_RE.findall(self.doc))
        for needed in ("/about/", "/contact/", "/privacy/", "/llms.txt", "/sitemap.xml"):
            self.assertIn(needed, hrefs)

    def test_stylesheet_is_shared_not_inline(self):
        self.assertNotIn("<style", self.doc)
        self.assertIn('<link rel="stylesheet" href="/assets/site.css">', self.doc)
        css = read("assets/site.css")
        self.assertIn(":root{", css)
        self.assertIn(':root[data-theme="dark"]{', css)
        self.assertIn(".page{", css)

    def test_markdown_twin_lists_every_project(self):
        twin = read("index.md")
        repos = {h for h in HREF_RE.findall(self.doc) if re.match(r"https://github\.com/Tatendaz/[^/]+$", h)}
        self.assertGreaterEqual(len(repos), 5)
        for repo in repos:
            self.assertIn(repo, twin, f"index.md is missing {repo}")
        self.assertIn("tatendaz@me.com", twin)


class EveryPageTests(unittest.TestCase):
    def test_title_canonical_and_description(self):
        for path, rel in PAGES.items():
            with self.subTest(page=path):
                doc = read(rel)
                title = re.search(r"<title>(.*?)</title>", doc, re.S).group(1)
                self.assertIn("Tatenda Zhou", html.unescape(title))
                canonical = [l for l in head_links(doc) if l.get("rel") == "canonical"]
                self.assertEqual([l["href"] for l in canonical], [f"{SITE}{path}"])
                self.assertTrue(meta_content(doc, "description"))
                self.assertEqual(meta_content(doc, "author"), "Tatenda Zhou")

    def test_markdown_alternate_points_at_existing_twin(self):
        for path, rel in PAGES.items():
            with self.subTest(page=path):
                doc = read(rel)
                alts = [l for l in head_links(doc) if l.get("rel") == "alternate" and l.get("type") == "text/markdown"]
                self.assertEqual(len(alts), 1, "exactly one text/markdown alternate")
                href = alts[0]["href"]
                self.assertEqual(href, f"{path}index.md")
                twin = ROOT / href.lstrip("/")
                self.assertTrue(twin.is_file(), f"{href} does not exist")
                body = twin.read_text(encoding="utf-8")
                self.assertTrue(body.startswith("# "), "Markdown twin must start with an H1")
                self.assertIn(f"HTML version: {SITE}{path}", body)
                self.assertIn(f"{SITE}/llms.txt", body)
                # llmstxt.org: rel="describedby" points at the llms.txt that covers the page.
                described = [l["href"] for l in head_links(doc) if l.get("rel") == "describedby"]
                self.assertEqual(described, ["/llms.txt"])

    def test_exactly_one_h1_inside_main(self):
        for path, rel in list(PAGES.items()) + [("/404", "404.html")]:
            with self.subTest(page=path):
                doc = read(rel)
                self.assertEqual(len(H1_RE.findall(doc)), 1)
                self.assertEqual(len(H1_RE.findall(main_html(doc))), 1)

    def test_no_boilerplate_elements_inside_main(self):
        # Readability-style extractors drop <header>/<nav>/<aside>/<footer> elements before
        # counting text and looking for the H1, so nothing that must count may live inside one.
        for path, rel in list(PAGES.items()) + [("/404", "404.html")]:
            with self.subTest(page=path):
                found = BOILERPLATE_TAG_RE.findall(main_html(read(rel)))
                self.assertEqual(found, [], f"boilerplate element(s) inside <main> on {path}: {found}")

    def test_boilerplate_and_hero_patterns_stop_at_tag_boundaries(self):
        # Near-miss markup must not match; \b-style boundaries would accept all of these.
        for near_miss in ("<header-card>", "<nav-item>", "<footer_note>", "<asideways>"):
            self.assertIsNone(BOILERPLATE_TAG_RE.search(near_miss), near_miss)
        for real in ("<header>", '<nav class="x">', "<footer/>", "<aside\n>"):
            self.assertIsNotNone(BOILERPLATE_TAG_RE.search(real), real)
        for near_miss in ('<div-thing class="hero">', '<div data-class="hero">',
                          '<div class="foo-hero">', '<div class="hero-card">'):
            self.assertIsNone(HERO_DIV_RE.search(near_miss), near_miss)
        for real in ('<div class="hero">', '<div class="card hero">', '<div id="top" class="hero card">'):
            self.assertIsNotNone(HERO_DIV_RE.search(real), real)

    def test_jsonld_blocks_are_valid(self):
        for path, rel in list(PAGES.items()) + [("/404", "404.html")]:
            with self.subTest(page=path):
                doc = read(rel)
                for block in ld_json_blocks(doc):  # json.loads raises on malformed JSON
                    self.assertEqual(block["@context"], "https://schema.org")
                    self.assertTrue(block.get("@type"))

    def test_shared_chrome_present(self):
        for path, rel in list(PAGES.items()) + [("/404", "404.html")]:
            with self.subTest(page=path):
                doc = read(rel)
                self.assertIn('id="themeToggle"', doc)
                self.assertIn('aria-pressed="false"', doc)
                self.assertIn("setAttribute('aria-pressed'", doc)
                self.assertIn("localStorage.getItem('theme')", doc)
                self.assertIn('<footer id="contact">', doc)
                self.assertIn('<link rel="stylesheet" href="/assets/site.css">', doc)
                self.assertIn('<meta name="viewport"', doc)
                self.assertNotIn("<style", doc)


class TrustPageTests(unittest.TestCase):
    def test_each_trust_page_has_500_plus_chars(self):
        for path in TRUST_PAGES:
            with self.subTest(page=path):
                text = visible_text(main_html(read(PAGES[path])))
                self.assertGreaterEqual(len(text), 500, f"{path} has only {len(text)} chars")

    def test_trust_page_specifics(self):
        about, contact, privacy = (read(PAGES[p]) for p in TRUST_PAGES)
        self.assertIn('href="/contact/"', about)
        self.assertIn("https://github.com/Tatendaz/promptups", about)
        self.assertIn("mailto:tatendaz@me.com", contact)
        self.assertIn("SECURITY.md", contact)
        for phrase in ("cookies", "GitHub Pages", "Google Fonts", "localStorage", "2026-08-22"):
            self.assertIn(phrase, privacy)

    def test_trust_page_jsonld_types(self):
        expected = {"/about/": "AboutPage", "/contact/": "ContactPage", "/privacy/": "WebPage"}
        for path, typ in expected.items():
            with self.subTest(page=path):
                block = ld_json_blocks(read(PAGES[path]))[0]
                self.assertEqual(block["@type"], typ)
                self.assertEqual(block["url"], f"{SITE}{path}")
                self.assertEqual(block["isPartOf"]["@id"], f"{SITE}/#website")
                if typ != "WebPage":
                    self.assertEqual(block["mainEntity"]["@id"], f"{SITE}/#person")


class NotFoundPageTests(unittest.TestCase):
    def setUp(self):
        self.doc = read("404.html")

    def test_is_short_noindex_and_points_agents_onward(self):
        self.assertIn("404", re.search(r"<title>(.*?)</title>", self.doc).group(1))
        self.assertEqual(meta_content(self.doc, "robots"), "noindex")
        text = visible_text(main_html(self.doc))
        self.assertLess(len(text), 1500, "keep the 404 body short")
        hrefs = set(HREF_RE.findall(self.doc))
        for needed in (f"{SITE}/", f"{SITE}/sitemap.xml", f"{SITE}/llms.txt", f"{SITE}/about/", f"{SITE}/contact/"):
            self.assertIn(needed, hrefs)
        for project in EXTERNAL_PROJECT_PATHS:
            self.assertIn(f"{SITE}/{project}/", hrefs)

    def test_markdown_pointer_block_for_agents(self):
        # The Is Agentic "Agent-friendly 404s" check gives full credit only when the 404 body
        # carries short Markdown guidance that points at the sitemap, llms.txt or a docs index.
        m = re.search(r'<pre class="md"[^>]*>(.*?)</pre>', main_html(self.doc), re.S)
        self.assertIsNotNone(m, "404 page needs a <pre class=\"md\"> Markdown block inside <main>")
        md = html.unescape(m.group(1)).strip()
        self.assertTrue(md.startswith("# 404"), md[:40])
        for line in ("## Where to look next", f"- [Site map]({SITE}/sitemap.xml)", f"- [llms.txt]({SITE}/llms.txt)",
                     f"[Home]({SITE}/)", f"[About]({SITE}/about/)", f"[Contact]({SITE}/contact/)"):
            self.assertIn(line, md)
        self.assertLess(len(md), 600, "keep the Markdown block short")
        self.assertNotRegex(md, r"<[a-z]+[\s>]", "the block must be plain Markdown, not HTML")

    def test_no_canonical_or_alternate(self):
        rels = {l.get("rel") for l in head_links(self.doc)}
        self.assertNotIn("canonical", rels)
        self.assertNotIn("alternate", rels)


class LlmsTxtTests(unittest.TestCase):
    def setUp(self):
        self.text = read("llms.txt")
        self.lines = self.text.splitlines()

    def test_llmstxt_org_structure(self):
        self.assertRegex(self.lines[0], r"^# \S")
        rest = [l for l in self.lines[1:] if l.strip()]
        self.assertTrue(rest[0].startswith("> "), "second block must be the blockquote summary")
        self.assertFalse([l for l in self.lines if re.match(r"^#{3,} ", l)], "only H1 and H2 headings allowed")
        h2s = [l for l in self.lines if l.startswith("## ")]
        self.assertIn("## When to use this site", h2s)
        if "## Optional" in h2s:
            self.assertEqual(h2s[-1], "## Optional", "Optional must be the last section")
        # Every H2 section is a file list: each bullet is "- [name](url): notes".
        section = None
        items_per_section: dict[str, int] = {}
        for line in self.lines:
            if line.startswith("## "):
                section = line
                items_per_section[section] = 0
            elif section and line.startswith("- "):
                self.assertRegex(line, LLMS_LINK_RE, f"bad list item in {section}: {line}")
                items_per_section[section] += 1
            elif section and line.strip():
                self.fail(f"non-list content inside {section}: {line!r}")
        for section, count in items_per_section.items():
            self.assertGreaterEqual(count, 1, f"{section} has no links")

    def test_when_to_use_is_specific(self):
        start = self.text.index("## When to use this site")
        end = self.text.index("\n## ", start + 1)
        block = self.text[start:end]
        self.assertGreaterEqual(block.count("\n- "), 3)
        for phrase in ("AI agents", "workshop", "Remote"):
            self.assertIn(phrase, block)

    def test_every_local_url_exists(self):
        urls = set(re.findall(rf"{re.escape(SITE)}(/[^\s)\]]*)", self.text))
        self.assertGreaterEqual(len(urls), 8)
        for path in sorted(urls):
            if path.startswith("/#"):
                continue
            target = local_file_for(path)
            if target is None:
                continue
            with self.subTest(path=path):
                self.assertTrue(target.is_file(), f"{path} -> {target.relative_to(ROOT)} missing")


class SitemapAndRobotsTests(unittest.TestCase):
    def test_sitemap_is_comment_free_and_lists_every_local_page(self):
        raw = read("sitemap.xml")
        self.assertNotIn("<!--", raw, "Google rejected the file while it carried a comment")
        lines = raw.splitlines()
        self.assertTrue(lines[0].startswith("<?xml"))
        self.assertTrue(lines[1].startswith("<urlset"))
        ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        root = ET.fromstring(raw)
        entries = root.findall("sm:url", ns)
        locs = [e.find("sm:loc", ns).text for e in entries]
        for path in PAGES:
            self.assertIn(f"{SITE}{path}", locs)
        for e in entries:
            with self.subTest(loc=e.find("sm:loc", ns).text):
                self.assertRegex(e.find("sm:lastmod", ns).text, r"^\d{4}-\d{2}-\d{2}$")
                loc = e.find("sm:loc", ns).text
                self.assertTrue(loc.startswith(SITE))
                target = local_file_for(loc[len(SITE):])
                if target is not None:
                    self.assertTrue(target.is_file(), f"{loc} has no file in this repo")
        self.assertEqual(len(locs), len(set(locs)), "duplicate <loc>")

    def test_robots_points_at_sitemap_and_llms(self):
        robots = read("robots.txt")
        self.assertIn(f"Sitemap: {SITE}/sitemap.xml", robots)
        self.assertIn(f"{SITE}/llms.txt", robots)
        self.assertIn("Allow: /", robots)
        self.assertNotRegex(robots, r"(?m)^Disallow: /\s*$", "no blanket disallow")


class MarkdownTwinTests(unittest.TestCase):
    def test_twins_are_plain_markdown_not_html(self):
        for path in PAGES:
            with self.subTest(page=path):
                body = (ROOT / f"{path.lstrip('/')}index.md").read_text(encoding="utf-8")
                self.assertNotRegex(body, r"<(div|span|script|style)\b", "twins must not contain HTML chrome")
                self.assertGreaterEqual(len(body), 500)


if __name__ == "__main__":
    unittest.main()
