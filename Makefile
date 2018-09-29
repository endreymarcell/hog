.PHONY: develop test report format lint typecheck check copy-hooks ci

develop:
	python3 -m venv virtualenv
	. virtualenv/bin/activate
	pip3 install -r requirements-dev.txt
	make copy-hooks
	make ci

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
