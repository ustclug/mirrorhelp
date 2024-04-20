.PHONY: all css

all: docs/contributor.md
	mkdocs build

css: docs/css/extra.css

docs/contributor.md: scripts/contributors.py
	python3 $^

docs/css/extra.css: docs/css/extra.scss
	scss -t compact $^ > $@
