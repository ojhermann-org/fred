# fred

A Python library for the [FRED API](https://fred.stlouisfed.org/docs/api/fred/) (Federal Reserve Economic Data, St. Louis Fed).

## Overview

`fred` provides a type-driven Python interface to the FRED API, built as self-contained modules:

1. **`request`**: builds typed, validated requests for the FRED API
2. **`response`**: models typed, validated responses from the FRED API

The two modules are intentionally independent — they share no code, including common types like `Realtime`.

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
import json
import urllib.parse
import urllib.request

from fred.request import FileType, RequestBuilder
from fred.response import SourceResponse

request = (
    RequestBuilder.source()(api_key="your-key", source_id=1, file_type=FileType.json)
    .build()
)
url = str(request.endpoint()) + "?" + urllib.parse.urlencode(request.parameters())

with urllib.request.urlopen(url) as resp:
    body = json.loads(resp.read().decode())

response = SourceResponse.model_validate(body)
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
