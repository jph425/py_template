# py_template
A template python project. Pre-configured for testing and building packages.

## 1. Project Setup
`requirements.txt` lists all imported dependencies needed to build and run the package.

`setup.cfg` lists package information used to builds the package. Use `pip install -e .` to build.

`setup.py` vestigial at this point, calls `setuptools.setup()`. Otherwise, nothing here.

`pyproject.toml` build configuration metadata.

## 2. Testing and Automation
We setup pytest, mypy, and tox here. Github actions are also configured to automatically run tests on push and pull-request.

The packages needed to run these processes, but NOT needed for running this package are listed in `requirements_dev.txt`.

### 2.1 pytest tests
[docs](https://docs.pytest.org)

`tests/conftest.py` contains pytest-specific fixtures needed for testing. This could be monkeypatches, static objects, or things that are big performance hits that can be cached for the entire pytest session.

`tests/test_*.py` contains any specific tests. Pytest will search this directory for any python file begining with "test_" and then runs it.

`setup.cfg` includes \[options.extras_require] to describe any additional packages needed for running tests.

`pyproject.toml` includes \[tools.pytest.*] to configure pytest features used (here: code coverage and the `tests/` path where pytest can find tests).

### 2.2 mypy type-checking
[docs](http://mypy-lang.org)

`setup.cfg` includes \[options.package_data] to specify the type hinting file (an empty file at creation, this template uses `src/py.typed`)

`pyproject.toml` includes \[tool.mypy] to configure mypy features and configuration. See mypy docs for full details.

### 2.3 tox testing matrix
[docs](https://tox.wiki/en/latest/)

`tox.ini` full configuration for tox runs. Automation information for tools tox should use for testin (pytest, mypy, github actions, flake8)

### 2.4 flake8 linting
[docs](https://flake8.pycqa.org/en/latest/)

`setup.cfg` can include any project-wide flake8 configuration needed. Here we set the max line length to 120 characters.

flake8 is pretty light on configuration. We just tell tox to run it in `tox.ini`. Otherwise you can run it with `flake8 src` (assuming flake8 is found in your environment). The flake8 docs include details on decorating your code to customize any parameters or exceptions to the PEP8 standards.

### 2.5 github actions & workflows
[docs](https://docs.github.com/en/actions)


---

![Tests](https://github.com/$USER/$PROJECT/actions/workflows/tests.yaml/badge.svg)
