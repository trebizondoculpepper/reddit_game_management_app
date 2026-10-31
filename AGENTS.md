# Reddit game management app

A small command-line tool for publicising a game on Reddit with as little upkeep as possible: posting release notes and devlogs to the game's subreddit (first r/the_pool_game, for The Pool, `/Users/salimfadhley/workspace/simulation_of_boring_things`), and keeping the subreddit's wiki and settings in step. Other projects install it with `uv tool install` and call it from their release scripts.

## Rules

- Python 3.14, managed with uv (`uv sync`, `uv run`, `uv add`). No pip, no requirements.txt, no Poetry.
- Source in `src/`, tests in `tests/` mirroring it, pytest. Type hints everywhere; mypy strict. Ruff for linting, black for formatting. Click for the CLI. Pathlib, not string paths.
- Never commit a secret: no client IDs, secrets, passwords or tokens in code, tests, fixtures, docs or CI files. They come from the environment or a config file outside the repository (see `doc/prompts/`). Tests never reach Reddit; they use fakes.
- Nothing posts for real without being asked: every command that changes Reddit has `--dry-run`, which prints exactly what it would send.
- Before committing: `uv run pytest`, `uv run mypy src`, `uv run ruff check`, `uv run black --check .`.
- Markdown is one paragraph per line, never hard-wrapped. UK spelling.
- Work is planned as numbered prompts in `doc/prompts/`; move a prompt to `doc/prompts/done/` when it is finished.
- Never commit `agent-mailbox.toml` or `agent-inbox.toml`.
