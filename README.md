# fred

A Python library for the [FRED API](https://fred.stlouisfed.org/docs/api/fred/) (Federal Reserve Economic Data, St. Louis Fed).

- [fred/v1](src/fred/v1/README.md)
- [builders/v1](src/builders/v1/README.md)
- [tofu](tofu/README.md)

## Overview

`fred` provides a type-driven Python interface to the FRED API. It is being built incrementally:

1. **Core library**: functional, type-driven approach for programmatic use
2. **Friendly wrapper**: minimal configuration (API key only), aimed at non-engineers

## Requirements

- [Nix](https://nixos.org/) with flakes enabled
- [direnv](https://direnv.net/) hooked into your shell
- An AWS SSO profile with access to the `FRED_API_KEY` secret in AWS Secrets Manager

## Getting started

1. Clone the repo and `cd` into it
2. Create `.env.local` and set your AWS SSO profile:
   ```bash
   export AWS_PROFILE=<your-aws-sso-profile>
   ```
3. Log in to AWS: `aws sso login`
4. Allow direnv: `direnv allow`

direnv will activate the nix dev shell, run `uv sync`, activate the Python venv, and export `FRED_API_KEY` automatically.

## Usage

```python
from fred import FredClient

# Explicit API key
client = FredClient(api_key="your-key")

# Or via environment variable (FRED_API_KEY)
client = FredClient()
```

## Development

### Running tests

```bash
# Unit tests only (no API key required)
pytest -m unit_test

# All tests (requires FRED_API_KEY)
pytest
```

### Pre-commit hooks

[prek](https://prek.j178.dev/) manages hooks. After cloning, hooks are activated automatically via `.git/hooks`. They run:

- **Pre-commit**: whitespace/file checks, nix checks (nixfmt, statix, deadnix), Python checks (ruff, ty)
- **Pre-push**: uv sync
