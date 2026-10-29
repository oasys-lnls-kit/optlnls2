<div align="center">

# OPTLNLS2

**Modular framework for X-ray optics, synchrotron radiation, and beamline design at Sirius/LNLS**

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/github/license/oasys-lnls-kit/optlnls2)
![Lint](https://img.shields.io/badge/lint-ruff-yellow)
![Format](https://img.shields.io/badge/format-ruff-yellow)
![Status](https://img.shields.io/badge/status-development-orange)
![Physics](https://img.shields.io/badge/domain-X--ray%20Optics-blueviolet)
![Facility](https://img.shields.io/badge/Sirius-LNLS-green)

</div>

---

OPTLNLS2 is a modular toolkit for X-ray optics, beamline design,
diagnostics, and synchrotron radiation calculations. The project aims
to provide a modern, maintainable, and extensible framework for the
development and operation of Sirius beamlines.

## Installation

```bash
git clone https://github.com/oasys-lnls-kit/optlnls2.git
cd optlnls2

pip install .
```

## How to use it?

This package is pip-installable, so the normal procedure for installation should be followed, like doing `pip install .` or `pip install -e .` after cloning the repository.

## Development

#### Tests

This package uses [`pytest`](https://docs.pytest.org/en/stable/) for running the tests, all available under the `tests/` folder. A CI pipeline also runs on every push to check that these tests do not break between commits.

#### Pre-commit

This package contains a [`pre-commit`](https://pre-commit.com/) file that checks for linting and formatting of Python code using [`ruff`](https://docs.astral.sh/ruff/) before comitting any changes. Having it enabled is a nice way to keep your code clean and organized, especially to make it easier for other people to read and contribute with your project.

To enable it, you need to install the pre-commit tool on your environment, with `pip install pre-commit`, and then, from the root of the project, where the `.pre-commit-config.yaml` file is located, run `pre-commit install`.
