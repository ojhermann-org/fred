variable "aws_role_arn" {
  description = "ARN of the IAM role to assume in the dev account"
  type        = string
  default     = "arn:aws:iam::916868258956:role/shared-jump-box-role"
}
