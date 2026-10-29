# optlnls2

Modular toolkit for X-ray optics, beamline design, diagnostics, and synchrotron radiation calculations.

## How to use it?

This package is pip-installable, so the normal procedure for installation should be followed, like doing `pip install .` or `pip install -e .` after cloning the repository.

## Development

#### Tests

This package uses [`pytest`](https://docs.pytest.org/en/stable/) for running the tests, all available under the `tests/` folder. A CI pipeline also runs on every push to check that these tests do not break between commits.

#### Pre-commit

This package contains a [`pre-commit`](https://pre-commit.com/) file that checks for linting and formatting of Python code using [`ruff`](https://docs.astral.sh/ruff/) before comitting any changes. Having it enabled is a nice way to keep your code clean and organized, especially to make it easier for other people to read and contribute with your project.

To enable it, you need to install the pre-commit tool on your environment, with `pip install pre-commit`, and then, from the root of the project, where the `.pre-commit-config.yaml` file is located, run `pre-commit install`.
