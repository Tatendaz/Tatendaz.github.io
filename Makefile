# Static site: no build step. `make test` runs the repo checks that CI runs.
.PHONY: test test-live serve

test:
	LIVE_SITE_URL= python3 -m unittest discover -s tests -v

# Checks the deployed site (status codes, content types, 404 body, sitemap URLs).
# Override the target with LIVE_SITE_URL=https://example.org make test-live
test-live:
	LIVE_SITE_URL=$${LIVE_SITE_URL:-https://tatendaz.github.io} python3 -m unittest tests.test_live -v

serve:
	python3 -m http.server 8000
