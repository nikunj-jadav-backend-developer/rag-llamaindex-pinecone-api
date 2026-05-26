provider "aws"{
    region = var.aws_region
}

data "aws_ami" "ubuntu_2204"{

    most_recent = true
    owners = ["099720109477"]  #Official Canonical Ubuntu AWS account ID

    filter{
        name = "name"
        values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
    }

    filter{
        name = "architecture"
        values = ["x86_64"]
    }

    filter{
        name = "virtualization-type"
        values = ["hvm"]
    }
}

resource "aws_security_group" "rag_sg" {
    name = "rag-app-sg"
    description = "Security group for RAG app"

    ingress{
        description = "SSH from my IP only"
        from_port = 22
        to_port = 22
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }

    ingress {
        description = "HTTP for Nginx later"
        from_port   = 80
        to_port     = 80
        protocol    = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }

    ingress {
        description = "HTTPS for SSL later"
        from_port   = 443
        to_port     = 443
        protocol    = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }
     egress {
        description = "Allow all outbound traffic"
        from_port   = 0
        to_port     = 0
        protocol    = "-1"
        cidr_blocks = ["0.0.0.0/0"]
    }

     tags = {
        Name = "rag-app-sg"
    }

}

resource "aws_key_pair" "rag_key" {
  key_name   = var.key_name
  public_key = file(var.public_key_path)
}

resource "aws_instance" "rag_server" {
    ami = data.aws_ami.ubuntu_2204.id
    instance_type = var.instance_type
    key_name      = var.key_name  
    associate_public_ip_address = true   
    vpc_security_group_ids = [aws_security_group.rag_sg.id]    
    tags = {
        Name = "rag-app-server"
    }                      
}