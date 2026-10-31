# 002: The Reddit CLI

Read `AGENTS.md` and finish `001` first.

## Goal

A low-maintenance way to publicise a game on Reddit: a CLI, `rgm`, that other projects install with `uv tool install` and call from their release scripts, posting release notes and devlogs to the game's subreddit and keeping its wiki in step. The first user is The Pool (`/Users/salimfadhley/workspace/simulation_of_boring_things`), whose `scripts/release-notes.ts` already builds Markdown release notes from `CHANGELOG.md`.

## Credentials (never in the repository)

- Reddit script app (client ID and secret) plus the posting account's username and password, created by the owner by hand.
- Read, in order of precedence: environment variables (`REDDIT_CLIENT_ID`, `REDDIT_CLIENT_SECRET`, `REDDIT_USERNAME`, `REDDIT_PASSWORD`, `REDDIT_USER_AGENT`), then a profile in a config file outside any repository (`~/.config/reddit-game-manager/config.toml`, chmod 600, the CLI refusing to read it if it is group- or world-readable), selected with `--profile`. Optionally the system keyring for the password and secret.
- `rgm auth check` logs in and prints who it is and which subreddits it moderates, without printing any secret. Secrets never appear in logs, errors or `--dry-run` output.
- It runs locally first (the owner, 2026-10-31): the credentials live only in the owner's config file. Running from GitHub Actions comes later (prompt 003), when the same environment variables will come from repository secrets; design for it now (no interactive-only paths, everything settable from the environment), but build no CI posting here.

## Commands (each that changes Reddit has `--dry-run`)

- `rgm post release --subreddit the_pool_game --title "The Pool v0.9.0 is out" --body notes.md [--flair Release] [--pin] [--link URL]`: a text post from a Markdown file (or `-` for stdin), with flair chosen by its text, optionally pinned (unpinning the previous pinned release post so only the latest stays), printing the post's URL.
- `rgm post link` and `rgm post image` for screenshots and links, with a title and flair.
- `rgm wiki put --subreddit ... --page changelog --body CHANGELOG.md --reason "v0.9.0"`: replace a wiki page; `rgm wiki get`.
- `rgm flair list` and `rgm flair ensure --from flair.toml`: create missing post flairs, idempotently.
- `rgm automod put --from automod.yaml`: write the AutoModerator config (a wiki page), validating it is YAML first.
- `rgm subreddit show` and `rgm subreddit apply --from subreddit.toml`: description, rules and settings from a file kept in the game's repo, applied idempotently, showing a diff first.

## Behaviour

- `post release` without `--yes` shows the post as `--dry-run` would and asks for confirmation before sending; `--yes` skips the question, for scripts.

- Idempotent where it can be: posting the same release title twice to the same subreddit refuses unless `--force`, so a re-run release job does not double-post.
- Reddit's rules on body length and rate limits are respected; a helpful error, not a traceback, on a failure.
- A thin wrapper module around praw, so the commands are tested against a fake of it; no test reaches Reddit. An optional, manually run smoke test (`-m live`, skipped by default) against a private test subreddit.
- `--json` output for scripts.

## Integration with The Pool (a follow-up, in that repo)

Document in the README how a game wires it in: `uv tool install git+https://github.com/trebizondoculpepper/reddit_game_management_app`, then, run locally after a release, `rgm post release ... --body <notes> --pin`, which shows the post and asks before sending. Leave The Pool's own changes to a prompt in that repository.

## Done when

All commands have tests against the fake; `rgm post release --dry-run` prints the exact post; the owner has run `rgm auth check` and one real post to r/the_pool_game; README documents setup, including creating the Reddit app, the config file and the GitHub secrets.
