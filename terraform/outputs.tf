output "ubuntu_ami_id" {
  value = data.aws_ami.ubuntu_2204.id
}

output "ec2_public_ip" {
  value = aws_instance.rag_server.public_ip
}

output "ssh_command" {
  value = "ssh -i ~/.ssh/${var.key_name}.pem ubuntu@${aws_instance.rag_server.public_ip}"
}