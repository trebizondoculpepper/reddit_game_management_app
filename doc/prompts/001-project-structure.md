# 001: Project structure, tests and CI

Read `AGENTS.md` first.

## Goal

Turn this directory into a well-formed uv project for Python 3.14, with an empty but working CLI, tests, type checking, linting and GitHub Actions CI, ready for prompt 002 to build the application into. No Reddit features yet.

## Steps

1. **pyproject.toml** (uv, `src` layout, build backend `uv_build`):
   - name `reddit-game-management-app`, import package `reddit_game_manager`, `requires-python = ">=3.14"`, a `.python-version` of `3.14`.
   - runtime dependencies: `praw` (latest, 8.x at the time of writing; check PyPI and pin `>=` the current release), `click`.
   - dev group (`uv add --group dev`): `pytest`, `pytest-cov`, `mypy`, `ruff`, `black`, `types-requests` if mypy needs it.
   - a console script: `rgm = "reddit_game_manager.cli:main"`.
   - tool config in pyproject: ruff (line length 100, a sensible rule set: E, F, I, B, UP, SIM), black (line length 100), mypy (`strict = true`; praw ships no type hints, so add an override with `ignore_missing_imports` for `praw.*`), pytest (`testpaths = ["tests"]`, `--strict-markers`).
2. **Layout**:
   ```
   src/reddit_game_manager/__init__.py   (__version__ from package metadata)
   src/reddit_game_manager/cli.py        (click group `main`, `--version`, a `hello`-free placeholder: just the group and version)
   src/reddit_game_manager/py.typed
   tests/test_cli.py                     (click's CliRunner: --help and --version work)
   README.md                             (what it is, install with `uv tool install`, development commands)
   CHANGELOG.md                          (Keep a Changelog, an Unreleased section)
   diary/                                (empty, with .gitkeep)
   ```
3. **CI** `.github/workflows/ci.yml`: on push and pull request; `astral-sh/setup-uv` (pin a version), `uv sync --locked`, then pytest with coverage, mypy, ruff check, black --check. Python from `.python-version`. No secrets used anywhere in CI.
4. **Pre-commit** (optional but preferred): a `.pre-commit-config.yaml` running ruff, black and mypy, documented in the README.
5. Commit `uv.lock`. Delete the stray `.venv` and re-create it with `uv sync`.
6. Check `uv tool install --editable .` gives a working `rgm --version` on the PATH, then uninstall it again (`uv tool uninstall reddit-game-management-app`).
7. Run every check in AGENTS.md; all green. Commit ("Project structure: uv, src layout, tests, CI").

## Done when

`uv sync && uv run pytest && uv run mypy src && uv run ruff check && uv run black --check .` all pass locally and in CI, and `rgm --version` works after a `uv tool install`.
