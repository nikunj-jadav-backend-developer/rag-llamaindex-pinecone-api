variable "aws_region" {
    description = "AWS region"
    type = string
    default = "ap-south-1"
}

variable "instance_type" {
    description = "EC2 instance type"
    type = string
    default = "t2.micro"    
}

variable "key_name" {
  description = "AWS EC2 key pair name"
  type        = string
}

variable "public_key_path" {
  description = "Path to local SSH public key file"
  type        = string
}

variable "my_ip" {
  description = "Your public IP with /32"
  type        = string
}
