# Development Diary Entry - 2026-10-31

## Context
- **Date**: 2026-10-31 UTC
- **Branch**: main
- **Contributors**: Claude Code + User

## Problem Statement
Prompt 001: turn the bare directory into a uv project for Python 3.14 with an empty but working `rgm` CLI, tests, strict typing, linting and CI, ready for prompt 002.

## Our Approach
A `src` layout built with `uv_build`, a click group with only `--version`, CliRunner smoke tests, and one GitHub Actions job running the same four checks as AGENTS.md.

## Implementation
- `pyproject.toml`: praw >=8.0.3 and click at runtime; pytest, pytest-cov, mypy, ruff, black and pre-commit in the dev group; ruff/black at line length 100, mypy strict with `praw.*` / `prawcore.*` import overrides.
- `src/reddit_game_manager/` (`__init__.py` with `__version__` from metadata, `cli.py`, `py.typed`), `tests/test_cli.py`, README, CHANGELOG.
- `.github/workflows/ci.yml` (setup-uv v7 pinned to uv 0.9.18, Python from `.python-version`, `uv sync --locked`, no secrets) and `.pre-commit-config.yaml` (ruff and black mirrors pinned to the locked versions, mypy as a local hook through `uv run`).

## Outcomes
- All checks green locally; 100% coverage of the two modules. `types-requests` was not needed.
- `uv_build` refuses to lock until `src/<module>/__init__.py` and the declared README exist, so the files have to come before `uv add`.
- With the project `.venv` on PATH, `which rgm` finds the venv's copy, not the tool's; the tool install was verified by running `$(uv tool dir --bin)/rgm` directly.
- CI has not run yet: the commit has not been pushed.

## Next Steps
Prompt 002: the Reddit CLI itself.
