terraform {
  required_version = ">= 1.8"

  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 6.0"
    }
  }

  backend "s3" {
    bucket         = "ojhermann-tofu-state-dev"
    key            = "fred/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "ojhermann-tofu-locks-dev"
    encrypt        = true
  }
}
