.PHONY: develop test report html format lint typecheck check copy-hooks ci distribute

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

html:
	coverage html && open htmlcov/index.html

format:
	black hog tests

lint:
	flake8 hog tests

typecheck:
	mypy hog tests

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

distribute:
	python3 setup.py sdist bdist_wheel
	python3 -m twine upload dist/*
