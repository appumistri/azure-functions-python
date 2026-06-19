output "function_app_default_host_name" {
  value       = azurerm_function_app.funcapp.default_host_name
  description = "Default hostname of your Function App"
}

output "storage_account_primary_web_endpoint" {
  value = azurerm_storage_account.storage.primary_web_endpoint
}