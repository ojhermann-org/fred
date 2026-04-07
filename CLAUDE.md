# fred — Claude Code guidance

## What this is

A Python library for the [FRED API](https://fred.stlouisfed.org/docs/api/fred/) (Federal Reserve Economic Data, St. Louis Fed).

The library is being built incrementally:
1. Core library: functional, type-driven approach
2. Friendly wrapper: requires only a valid API key; aimed at non-engineers

## Tech stack

- **Nix flakes**: manages high-level dev dependencies (uv, prek, helix LSPs, awscli2, etc.)
- **uv**: manages Python dependencies (`pyproject.toml`), lib layout (`src/fred/`)
- **direnv**: activates the nix dev shell and loads secrets automatically on `cd`
- **prek**: pre-commit and pre-push hooks

## Development workflow

Enter the dev environment by `cd`-ing into the repo — direnv activates everything automatically via `.envrc`. You must have:
- `direnv` installed and hooked into your shell
- An AWS SSO profile set in `.env.local` (see below)

### First-time setup

1. Copy `.env.local.example` (or create `.env.local`) and set your AWS profile:
   ```
   export AWS_PROFILE=<your-aws-sso-profile>
   ```
2. Log in to AWS SSO: `aws sso login`
3. `cd` into the repo — direnv will run `uv sync`, activate the venv, and export `FRED_API_KEY`

### Commits and pushes

prek hooks run automatically. Pre-commit checks: builtins, nix (nixfmt, statix, deadnix), Python (ruff, ty). Pre-push: uv sync.

## AWS and secrets

- `FRED_API_KEY` is stored in AWS Secrets Manager in the `otto-dev` account under the secret name `fred/api-key`
- Contributors need an AWS SSO profile with `secretsmanager:GetSecretValue` access to that secret
- `.env.local` (gitignored) is where each contributor sets their `AWS_PROFILE`
- CI uses GitHub Actions OIDC to assume an IAM role in the `otto-dev` account and fetch the secret — **this is not yet wired up**; for now, integration tests are skipped in CI

## Testing

Two tiers:
- **Unit tests** (`-m unit_test`): mock the HTTP layer, no API key needed, always run
- **Integration tests**: require `FRED_API_KEY` to be set, skipped if absent

Run unit tests: `pytest -m unit_test`
Run all tests (requires API key): `pytest`

## Library API design

The library accepts the API key as an explicit parameter first, with an optional fallback to the `FRED_API_KEY` environment variable:

```python
client = FredClient(api_key="...")        # explicit
client = FredClient()                     # reads FRED_API_KEY from environment
```

Never log or expose the API key in debug output, request metadata, or error messages.

## Git workflow

All changes on a branch, merged via PR. See global `~/.claude/CLAUDE.md` for org-wide conventions.
