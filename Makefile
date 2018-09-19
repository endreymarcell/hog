.PHONY: test report format lint typecheck check copy-hooks ci

test:
	coverage run -m unittest

report:
	coverage report

format:
	black .

lint:
	flake8

typecheck:
	mypy src tests

check:
	make format
	make lint
	make typecheck
	make test
	make report

copy-hooks:
	cp .githooks/* .git/hooks/

ci:
	make lint
	make typecheck
	make test
