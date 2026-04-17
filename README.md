# fred

> **Work in progress** — the library is being built incrementally. APIs will change as more endpoints are added.

A Python library for the [FRED API](https://fred.stlouisfed.org/docs/api/fred/) (Federal Reserve Economic Data, St. Louis Fed).

## Overview

`fred` provides a type-driven Python interface to the FRED API. It is built endpoint by endpoint, with a typed request params model and a typed response model for each endpoint.

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

Fetch the root FRED category:

```python
import json
import urllib.parse
import urllib.request

from fred import category, for_request

params = category.RequestParams(
    api_key="your-api-key",
    file_type=category.FileType.json,
    category_id=0,
)

url = f"{category.ENDPOINT}?{urllib.parse.urlencode(for_request(params))}"

with urllib.request.urlopen(url) as resp:
    data = json.loads(resp.read())

response = category.Response.model_validate(data)
print(response.categories[0].name)  # "Categories"
```

## Development

### Running tests

```bash
# Unit and contract tests (no API key required)
pytest -m "unit_test or contract_test"

# All tests (requires FRED_API_KEY)
pytest
```

### Pre-commit hooks

[prek](https://prek.j178.dev/) manages hooks. After cloning, hooks are activated automatically via `.git/hooks`. They run:

- **Pre-commit**: whitespace/file checks, nix checks (nixfmt, statix, deadnix), Python checks (ruff, ty)
- **Pre-push**: uv sync
