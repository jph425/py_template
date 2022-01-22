# py_template
A template python project. Pre-configured for testing and building packages.

## 1. Project Setup
`requirements.txt` lists all imported dependencies needed to build and run the package. It's good form to be very specific with versions here.

`requirements_dev.txt` lists any additional dependencies needed to run the automated testing or for other development activities. This list augments `requirements.txt` for testing.

`setup.cfg` lists package information used to builds the package. This is the **only** place to edit the version strings of packages (see `__init__.py` for details). dependencies are listed here too, it should be the same set of packages as `requirements.txt` + `requirements_dev.txt` but versions not critical here.

`setup.py` vestigial at this point, calls `setuptools.setup()`. Otherwise, nothing here.

`pyproject.toml` build configuration metadata for LOTS of these automated tools.

### 1.1 Building and Testing
 - Build the project locally for development with `pip install -e .`

 - Build for release with `python setup.py bdist_wheel` and/or `python setup.py sdist`

 - Run the linter with `flake8 src`

 - Run the type-checker with `mypy src`

 - Run the tests with `pytest .`

 - Run the tests, linter, and type-checker with `tox`. It might be useful to use `tox --parallel auto` to speed up this process.

## 2. Testing and Automation
We setup pytest, mypy, and tox here. Github actions are also configured to automatically run tests on push and pull-request.

The packages needed to run these processes, but NOT needed for running this package are listed in `requirements_dev.txt`.

### 2.1 pytest tests
[docs](https://docs.pytest.org)

`tests/conftest.py` contains pytest-specific fixtures needed for testing. This could be monkeypatches, static objects, or things that are big performance hits that can be cached for the entire pytest session.

`tests/test_*.py` contains any specific tests. Pytest will search this directory for any python file begining with "test_" and then runs it.

`setup.cfg` includes \[options.extras_require] to describe any additional packages needed for running tests.

`pyproject.toml` includes \[tools.pytest.*] to configure pytest features used (here: code coverage and the `tests` path where pytest can find tests).

Output is found in stdout and summarized after the suite has run. Tox will summarize the summary, and list specifica failures. Coverage is also summarized with the test results. `.coverage` is a cache file created by pytest. In addition, pytest builds an sdist for the project, so it will also create `src/package_name.egg_info`, and possibly `build` and `dist` depending on configuration.

### 2.2 mypy type-checking
[docs](http://mypy-lang.org)

`setup.cfg` includes \[options.package_data] to specify the type hinting file (an empty file at creation, this template uses `src/py.typed`)

`pyproject.toml` includes \[tool.mypy] to configure mypy features and configuration. See mypy docs for full details. (note that mypy looks in several places for configuration, searching in order: `mypy.ini`, `.mypy.ini`, `pyproject.toml`, `setup.cfg`, `$CDG_CONFIG_HOME/mypy/config`, `~/.config/mypy/config`, `~/.mypy.ini`)

Output is listed in stdout or tox if any issues are found. Reports are in plain text at `mypyCoverageReport/*`. Various other ancillary files are found at `.mypy_cache/*`.

### 2.3 tox testing matrix
[docs](https://tox.wiki/en/latest/)

`tox.ini` full configuration for tox runs. Automation information for tools tox should use for testing (pytest, mypy, github actions, flake8)

### 2.4 flake8 linting
[docs](https://flake8.pycqa.org/en/latest/)

`setup.cfg` can include any project-wide flake8 configuration needed. Here we set the max line length to 120 characters.

flake8 is pretty light on configuration. We just tell tox to run it in `tox.ini`. Otherwise you can run it with `flake8 src` (assuming flake8 is found in your environment). The flake8 docs include details on decorating your code to customize any parameters or exceptions to the PEP8 standards.

Output is silent on pass, and fatal with error messages in stdout for failures.

### 2.5 github actions & workflows
[docs](https://docs.github.com/en/actions)


---

![Tests](https://github.com/jph425/py_template/actions/workflows/tests.yaml/badge.svg)
