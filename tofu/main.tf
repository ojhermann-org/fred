data "github_organization_teams" "all" {}

locals {
  admins_team_id = one([
    for team in data.github_organization_teams.all.teams : team.id
    if team.slug == "admins"
  ])
}

resource "github_repository_environment" "integration" {
  environment = "integration"
  repository  = "fred"

  reviewers {
    teams = [local.admins_team_id]
  }
}

resource "github_actions_environment_variable" "aws_role_arn" {
  environment  = github_repository_environment.integration.environment
  repository   = "fred"
  variable_name = "AWS_ROLE_ARN"
  value        = "arn:aws:iam::916868258956:role/fred-github-actions"
}
