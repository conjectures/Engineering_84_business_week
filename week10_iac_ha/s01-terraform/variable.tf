
# VPC vars
variable "vpc_name" {
  default = "eng84_alexis_terraform_vpc"
}

# Subnet Vars
variable "subnet_name" {
  default = "eng84_alexis_terraform_subnet"
}

# Application vars
variable "application_name" {
  default = "eng84_alexis_terraform_application"
}

variable "webapp_ami_id" {
  default = "ami-042af9229265c27d0"
}

# Security Group vars
variable "security_group_name" {
  default = "eng84_alexis_terraform_public_sg"
}

