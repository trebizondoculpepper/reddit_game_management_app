# 003: Post release notes from GitHub Actions

Read `AGENTS.md`; do this after `002` has been used locally for at least one real release.

## Goal

When a game's release workflow publishes a release, it posts the release notes to the game's subreddit automatically, with no step on the owner's machine.

## Steps

1. A reusable composite action (`.github/actions/post-release/action.yml`) or a documented workflow snippet: `astral-sh/setup-uv`, `uv tool install git+https://github.com/trebizondoculpepper/reddit_game_management_app@<tag>` (pinned to a release of this tool, never `main`), then `rgm post release --yes --pin ...` with the notes file the game's workflow built.
2. Credentials from the game repository's secrets (`REDDIT_CLIENT_ID`, `REDDIT_CLIENT_SECRET`, `REDDIT_USERNAME`, `REDDIT_PASSWORD`), passed as environment variables to that one step only; `REDDIT_USER_AGENT` may be a plain variable. Document setting them with `gh secret set` (the owner types the values; no agent handles them).
3. Safe to re-run: the double-post check from 002 makes a retried job a no-op; a failure to post never fails the release itself (`continue-on-error`, with a warning annotation and the dry-run text in the job summary so the owner can post by hand).
4. A `workflow_dispatch` input `dry_run` (default true until the owner turns it off), so the first runs only show what would be posted.
5. Write the matching prompt for The Pool's repository (`doc/prompts/` there): add the step to its `release.yml` after the itch.io upload, using the notes from `scripts/release-notes.ts`.

## Done when

A test release in a scratch repository posts (or, with `dry_run`, shows) the right post; the README documents the action, the secrets and the dry-run switch.
