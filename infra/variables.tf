variable "location" {
  description = "Azure region to deploy into"
  type        = string
  default     = "eastus"
}

variable "prefix" {
  description = "String prefix for all resources"
  type        = string
  default     = "func-demo"
}