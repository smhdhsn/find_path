.PHONY: run lint

run:
	@python -m main

lint:
	@pylint --ignore=.venv .
