PYTHON = .venv/bin/python
PIP = .venv/bin/pip
SOURCE = a_maze_ing.py config.py generate_maze.py
MAIN = a_maze_ing.py
CONFIG = config.txt

.PHONY: install run debug clean lint lint-strict build

install:
	python3 -m venv .venv
	$(PIP) install -r requirement.txt

run:
	$(PYTHON) $(MAIN) $(CONFIG)

debug:
	$(PYTHON) -m pdb $(MAIN)

clean:
	rm -rf .venv build dist
	find . -type d \( -name "*.egg-info" -o -name "__pycache__" -o -name ".mypy_cache" -o -name ".pytest_cache" \) -prune -exec rm -rf {} +
	find . -type f \( -name "*.pyc" -o -name "*.pyo" \) -delete

lint:
	.venv/bin/flake8 $(SOURCE)
	.venv/bin/mypy $(SOURCE) --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	.venv/bin/flake8 $(SOURCE)
	.venv/bin/mypy $(SOURCE) --strict

build:
	$(PYTHON) -m build


