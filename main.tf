# Initialise terraform

# Providers

# Launch an EC2 instancs

# Define the cloud provider, initialise and install plugins based on provider
provider "aws"{
  # Define region
  region = "eu-west-1"
}


# Create vpc
resource "aws_vpc" "alexis_vpc" {
  cidr_block = "12.1.0.0/16"
  instance_tenancy = "default"
  tags = {
    Name = var.vpc_name
  }
}

resource "aws_subnet" "alexis_subnet" {
  vpc_id = aws_vpc.alexis_vpc.id
  cidr_block = "12.1.1.0/24"

tags = {
  Name = var.subnet_name

  }
}

resource "aws_security_group" "alexis_public_sg" {
  name = var.security_group_name
  description =  "public security group"
  vpc_id = aws_vpc.alexis_vpc.id

  ingress {
    from_port = "80"
    to_port = "80"
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"] 
  }
  egress {
    from_port = 0
    to_port = 0
    protocol = "-1"   # allow all
    cidr_blocks = ["0.0.0.0/0"] 
  }

  tags = {
    Name = var.security_group_name
  }
}


# Block of code for resource
resource "aws_instance" "app_instance" {

  # AMI image for server
  ami = "ami-042af9229265c27d0"

  # Instance type
  instance_type = "t2.micro"

  # public IP
  associate_public_ip_address = true

  # Subnet 
  subnet_id = aws_subnet.alexis_subnet.id
  # Security Groups
  vpc_security_group_ids = [aws_security_group.alexis_public_sg.id]


  # Tags to be passed to instance
  tags = {
    Name = var.application_name
  }
}

data "template_file" "app_init" {
  template = "${file("./scripts/app/init.sh.tpl")}"
}
