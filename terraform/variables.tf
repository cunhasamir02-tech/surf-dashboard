variable "aiven_api_token" {
  type      = string
  sensitive = true
}

variable "aiven_project" {
  type = string
}

variable "cloud_name" {
  type    = string
  default = "google-southamerica-east1"
}

variable "pg_plan" {
  type    = string
  default = "hobbyist"
}

variable "service_name" {
  type    = string
  default = "surf-dashboard-pg"
}
