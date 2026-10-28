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

resource "aiven_pg_database" "surf" {
  project       = var.aiven_project
  service_name  = aiven_pg.surf_db.service_name
  database_name = var.database_name
}

resource "aiven_pg_user" "surf_user" {
  project      = var.aiven_project
  service_name = aiven_pg.surf_db.service_name
  username     = var.db_username
}
