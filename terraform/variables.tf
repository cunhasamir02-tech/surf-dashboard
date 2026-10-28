variable "aiven_api_token" {
  description = "Token de API da Aiven"
  type        = string
  sensitive   = true
}

variable "aiven_project" {
  description = "Nome do projeto na Aiven"
  type        = string
}

variable "cloud_name" {
  description = "Região/nuvem da Aiven"
  type        = string
  default     = "google-southamerica-east1"
}

variable "pg_plan" {
  description = "Plano do serviço PostgreSQL"
  type        = string
  default     = "hobbyist"
}

variable "service_name" {
  description = "Nome do serviço PostgreSQL"
  type        = string
  default     = "surf-dashboard-pg"
}

variable "database_name" {
  description = "Nome do banco de dados"
  type        = string
  default     = "surfdb"
}

variable "db_username" {
  description = "Usuário de aplicação"
  type        = string
  default     = "surf_app"
}
