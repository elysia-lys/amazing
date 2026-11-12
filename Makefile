PYTHON = .venv/bin/python
PIP = .venv/bin/pip
SOURCE = #test.py

.PHONY: install run debug clean lint lint-strict

install: 
	python3 -m venv .venv
	$(PIP) install -r requirement.txt

run:
	$(PYTHON) $(SOURCE)

debug:
	$(PYTHON) -m pdb $(SOURCE)

clean:
	rm -rf .venv
	find . -type d \( -name __pycache__ -o -name .mypy_cache -o -name .pytest_cache \) -prune -exec rm -rf {} +
	find . -type f \( -name "*.pyc" -o -name "*.pyo" \) -delete

lint:
	.venv/bin/flake8 $(SOURCE)
	.venv/bin/mypy $(SOURCE) --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	.venv/bin/flake8 $(SOURCE)
	.venv/bin/mypy $(SOURCE) --strict




