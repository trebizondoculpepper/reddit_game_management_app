# Reddit game management app

`rgm` is a small command-line tool for publicising a game on Reddit with as little upkeep as possible: posting release notes and devlogs to the game's subreddit, and keeping the subreddit's wiki and settings in step. The first user is [r/the_pool_game](https://www.reddit.com/r/the_pool_game/), for The Pool.

No Reddit features exist yet; this is the project skeleton.

## Install

Other projects install it as a uv tool and call it from their release scripts:

```bash
uv tool install git+https://github.com/trebizondoculpepper/reddit_game_management_app
rgm --version
```

From a local checkout, `uv tool install --editable .` does the same.

## Development

Requires [uv](https://docs.astral.sh/uv/) and Python 3.14.

```bash
uv sync                    # create .venv with runtime and dev dependencies
uv run rgm --help          # run the CLI
uv run pytest              # tests, with coverage: uv run pytest --cov
uv run mypy src            # strict type checking
uv run ruff check          # lint
uv run black --check .     # formatting
```

All four checks must pass before committing; CI runs the same ones on every push and pull request.

### Pre-commit

The repository has a `.pre-commit-config.yaml` that runs ruff, black and mypy. Install the hook once per checkout:

```bash
uv run pre-commit install
uv run pre-commit run --all-files   # check everything by hand
```

## Secrets

No Reddit credentials ever go in this repository. They come from the environment or a config file outside it.
