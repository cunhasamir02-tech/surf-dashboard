output "pg_service_uri" {
  value     = aiven_pg.surf_db.service_uri
  sensitive = true
}
