# tofu

OpenTofu configuration for the `fred` repository's GitHub and AWS infrastructure.

## What this manages

- **GitHub Actions environment** (`integration`): gates access to AWS credentials behind a reviewer approval step
- **Environment variable** (`AWS_ROLE_ARN`): the IAM role ARN that the `integration_tests` CI job assumes via OIDC

## State

Remote state is stored in S3 (`ojhermann-tofu-state-dev` bucket, key `fred/terraform.tfstate`) with DynamoDB locking.

## Usage

```bash
tofu init
tofu plan
tofu apply   # ask Otto to run after merging
```

## CI

The `integration_tests` job in `.github/workflows/ci.yml` runs after `prek` passes. It authenticates to AWS using OIDC, fetches `FRED_API_KEY` from Secrets Manager, and runs the integration test suite.

Because the job is scoped to the `integration` environment, a reviewer must approve each run before it executes — preventing untrusted code from accessing AWS credentials.

```mermaid
sequenceDiagram
    participant PR as Pull Request
    participant prek as prek job
    participant reviewer as Reviewer
    participant GH as integration_tests job
    participant AWS as AWS (OIDC + STS)
    participant SM as Secrets Manager
    participant FRED as FRED API

    PR->>prek: trigger on pull_request
    prek-->>GH: pass (needs: prek)
    GH->>reviewer: request approval (integration environment)
    reviewer-->>GH: approve
    GH->>AWS: assume fred-github-actions role via OIDC
    AWS-->>GH: temporary credentials
    GH->>SM: get-secret-value fred/api-key
    SM-->>GH: FRED_API_KEY
    GH->>FRED: pytest -m integration_test
    FRED-->>GH: response
    GH-->>PR: pass / fail
```
