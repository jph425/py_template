# Paths
VENV = ./venv
SRC = ./src
TESTS = ./tests

# File lists
SRC_PY = $(wildcard $(SRC)/package_name/*.py)
TESTS_PY = $(wildcard $(TESTS)/*.py)
REQ = requirements_dev.txt requirements.txt
DOC_CONFIG = 
CONFIG = pyproject.toml setup.py setup.cfg tox.ini LICENSE $(REQ) $(DOC_CONFIG)

# Command macros
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
RM = rm -f
TOX = tox


# Create a development environment with the latest
# version of package_name installed. This should be
# run again after any changes to package metadata
# (e.g. setup.cfg, pypackage.toml)
install: $(SRC_PY) $(CONFIG) $(VENV)/bin/activate
	@echo "=== INSTALLING PACKAGE FOR DEVELOPMENT ==="
	@echo "  - the package will be installed in the venv at $(VENV)"
	@echo "  - the package will be installed in editable mode"
	$(PIP) install -e .


# venvs are cool
$(VENV)/bin/activate: $(REQ)
	@echo "=== CREATING VENV ==="
	python3 -m venv venv
	$(PIP) install -r requirements.txt
	$(PIP) install -r requirements_dev.txt


all: install test docs


# Delete all the files created by these other
# targets, back to a clean working directory.
.PHONY: clean
clean:
	@echo "=== CLEANING UP ==="
	-$(RM) -r $(SRC)/package_name/__pycache__
	-$(RM) -r $(VENV)
	-$(RM) -r mypyCoverageReport
	-$(RM) -r .tox
	-$(RM) -r .mypy_cache
	-$(RM) -r $(SRC)/package_name.egg-info
	-$(RM) -r $(TESTS)/__pycache__
	-$(RM)  .coverage


# Generate documentation using whatever system
docs: $(SRC_PY) $(DOC_CONFIG)
# Use sphinx or mkdoc here, you do you.
# Don't forget to update the clean target
# if needed.
	@echo "=== GENERATING DOCS ==="
	@echo "  - currently no docs exist"


# Run the tox test suite, including unit tests, 
# code coverage, type checking, and linting reports.
test: $(SRC_PY) $(TESTS_PY) $(CONFIG)
	@echo "=== RUNNING TOX TEST SUITE ==="
	$(TOX) -p auto
