terraform {
  required_providers {
    aiven = {
      source  = "aiven/aiven"
      version = "~> 4.0"
    }
  }
}

provider "aiven" {
  api_token = var.aiven_api_token
}

resource "aiven_pg" "surf_db" {
  project                 = var.aiven_project
  cloud_name              = var.cloud_name
  plan                    = var.pg_plan
  service_name            = var.service_name
  maintenance_window_dow  = "sunday"
  maintenance_window_time = "03:00:00"
}
