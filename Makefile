test:
	python3.11 -m pytest tests

lint:
	python3.11 -m flake8 duckingit tests

build:
	python3.11 -m build

upload:
	python3.11 -m twine upload dist/*

clean:
	rm -rf dist/
	rm -rf *.egg-info
