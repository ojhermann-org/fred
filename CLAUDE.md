# fred — Claude Code guidance

## What this is

A Python library for the [FRED API](https://fred.stlouisfed.org/docs/api/fred/) (Federal Reserve Economic Data, St. Louis Fed).

The library lives under `src/fred/` and is built incrementally, endpoint by endpoint. The top-level subpackages are:
- `fred.enums` — enum types (e.g. `FileType`, `Endpoint`)
- `fred.types` — primitive types and per-endpoint request/response models (e.g. `CategoryRequestParams`, `Category`, `CategoryResponse`)
- `fred.functions` — small utility functions (e.g. `today_st_louis`)

Each endpoint gets a `*RequestParams` model and a `*Response` model. Both are Pydantic `BaseModel`s. Use `fred.functions.for_request` to serialize a `*RequestParams` model to a `dict[str, str]` for use in a request. Enums, primitive types, and other shared building blocks live in `fred.enums` and `fred.types` respectively.

## Tech stack

- **Nix flakes**: manages high-level dev dependencies (uv, prek, helix LSPs, awscli2, etc.)
- **uv**: manages Python dependencies (`pyproject.toml`), lib layout (`src/`)
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

Three tiers:
- **Unit tests** (`-m unit_test`): no API key needed, always run
- **Contract tests** (`-m contract_test`): assert on specific values (e.g. enum values), no API key needed, always run
- **Integration tests** (`-m integration_test`): require `FRED_API_KEY` to be set, skipped if absent; live in `tests/integration_test/`

Run unit and contract tests: `pytest -m "unit_test or contract_test"`
Run all tests (requires API key): `pytest`

## Library API design

Each subpackage exposes a minimal public API via its `__init__.py`. Implementation details are kept internal. Never log or expose the API key in debug output, request metadata, or error messages.

## Git workflow

All changes on a branch, merged via PR. See global `~/.claude/CLAUDE.md` for org-wide conventions.
