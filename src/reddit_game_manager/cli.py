"""Command-line entry point for ``rgm``."""

import click

from reddit_game_manager import __version__


@click.group()
@click.version_option(__version__, prog_name="rgm")
def main() -> None:
    """Post release notes and devlogs to a game's subreddit and keep it in step."""
