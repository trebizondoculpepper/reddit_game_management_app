"""Smoke tests for the ``rgm`` command-line interface."""

from click.testing import CliRunner

from reddit_game_manager import __version__
from reddit_game_manager.cli import main


def test_help_shows_usage() -> None:
    result = CliRunner().invoke(main, ["--help"])
    assert result.exit_code == 0
    assert "Usage:" in result.output


def test_version_prints_package_version() -> None:
    result = CliRunner().invoke(main, ["--version"])
    assert result.exit_code == 0
    assert result.output.strip() == f"rgm, version {__version__}"
