# tofu

OpenTofu configuration for the `fred` repository's GitHub Actions environment.

## What this manages

- **GitHub Actions environment** (`integration`): gates the `integration_tests` CI job behind admin-team reviewer approval

## State

Remote state is stored in S3 (`ojhermann-tofu-state-dev` bucket, key `fred/terraform.tfstate`) with DynamoDB locking.

## Usage

```bash
tofu init
tofu plan
tofu apply   # a member of the ojhermann-org admin team can run this after merging
```

## CI

The `integration_tests` job in `.github/workflows/ci.yml` reads `FRED_API_KEY` from a GitHub Actions environment secret on the `integration` environment. Because the job is scoped to that environment, a reviewer must approve each run before it executes — preventing untrusted code from accessing the secret.
