data "github_user" "ojhermann" {
  username = "ojhermann"
}

resource "github_repository_environment" "integration" {
  environment = "integration"
  repository  = "fred"

  reviewers {
    users = [data.github_user.ojhermann.id]
  }
}

resource "github_actions_environment_variable" "aws_role_arn" {
  environment  = github_repository_environment.integration.environment
  repository   = "fred"
  variable_name = "AWS_ROLE_ARN"
  value        = "arn:aws:iam::916868258956:role/fred-github-actions"
}
