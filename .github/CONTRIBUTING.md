# Contributing to LangChain Zero to Hero

Hi there! Thank you for even being interested in contributing to this tutorial series.

## 🚀 Quick Start

This project uses [Poetry](https://python-poetry.org/) as a dependency manager. Check out Poetry's [documentation on how to install it](https://python-poetry.org/docs/#installation) on your system before proceeding.

❗Note: If you use `Conda` or `Pyenv` as your environment / package manager, avoid dependency conflicts by doing the following first:
1. *Before installing Poetry*, create and activate a new Conda env (e.g. `conda create -n langchain python=3.9`)
2. Install Poetry (see above)
3. Tell Poetry to use the virtualenv python environment (`poetry config virtualenvs.prefer-active-python true`)
4. Continue with the following steps.

To install requirements:

```bash
make install
```

This will install all requirements for running the package, examples, linting, formatting, tests, and coverage.

❗Note: If you're running Poetry 1.4.1 and receive a `WheelFileValidationError` for `debugpy` during installation, you can try either downgrading to Poetry 1.4.0 or disabling "modern installation" (`poetry config installer.modern-installation false`) and re-install requirements. See [this `debugpy` issue](https://github.com/microsoft/debugpy/issues/1246) for more details.

Now, you should be able to run the common tasks in the following section.

## ✅ Common Tasks

Type `make` for a list of common tasks.

### Code Formatting

Formatting for this project is done via a combination of [Black](https://black.readthedocs.io/en/stable/) and [isort](https://pycqa.github.io/isort/) via [pre-commit](https://pre-commit.com/).

To run formatting for this project:

```bash
make pre-commit
```

### Testing

To run unit tests:

```bash
make test
```

If you add new logic, please add a unit test.

## 🏭 Release Process

TBD
