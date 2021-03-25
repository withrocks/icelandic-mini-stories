pages:
	@python src/split.py src/All-60-mini-stories-EN.md en
	@python src/split.py src/All-60-mini-stories-IS.md is
	@python src/format-index.py > index.md

