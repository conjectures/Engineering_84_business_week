# Initialise terraform

# Providers

# Launch an EC2 instancs

# Define the cloud provider, initialise and install plugins based on provider
provider "aws"{
  # Define region
  region = "eu-west-1"
}

# # Block of code for resource
# resource "aws_instance" "app_instance" {
# 
#   # AMI image for server
#   ami = "ami-042af9229265c27d0"
# 
#   # Instance type
#   instance_type = "t2.micro"
# 
#   # public IP
#   associate_public_ip_address = true
# 
#   # Tags to be passed to instance
#   tags = {
#     Name = "eng84_alexis_application_terraform"
#   }
# 
# }

resource "aws_vpc" "alexis" {
  cidr_block = "12.1.0.0/16"
  instance_tenancy = "default"
  tags = {
    Name = "eng84_alexis_vpc_terraform"
  }
}

resource "aws_subnet" "random" {
  vpc_id = aws_vpc.alexis.id
  cidr_block = "12.1.1.0/24"

tags = {
  Name = "eng84_alexis_subnet_public"

  }
}
