terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

variable "region" {
  type        = string
  description = "AWS region to target (example only)."
  default     = "us-east-1"
}

variable "db_identifier" {
  type        = string
  description = "Identifier for the database instance."
  default     = "example-postgres"
}

variable "db_username" {
  type        = string
  description = "Master username (example only)."
  default     = "app"
}

variable "db_password" {
  type        = string
  description = "Master password (example only). Use secrets in real setups."
  sensitive   = true
  default     = "change-me"
}

provider "aws" {
  region = var.region
}

# Example-only: minimal RDS Postgres definition to show structure and guardrails.
# This is intended to be validated (`terraform validate`), not applied by default.
resource "aws_db_instance" "postgres" {
  identifier = var.db_identifier

  engine         = "postgres"
  engine_version = "16.3"

  instance_class = "db.t4g.micro"
  allocated_storage = 20

  username = var.db_username
  password = var.db_password

  publicly_accessible = false
  deletion_protection = true

  backup_retention_period = 7
  skip_final_snapshot     = true
}

