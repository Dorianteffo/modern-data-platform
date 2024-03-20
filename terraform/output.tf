output "ec2_public_dns" {
  description = "EC2 public dns"
  value       = aws_instance.sde_ec2.public_dns
}


output "airflow_ec2_public_dns" {
  description = "EC2 public dns"
  value       = aws_instance.airflow_ec2.public_dns
}


output "private_key" {
  description = "EC2 private key"
  value       = tls_private_key.custom_key.private_key_pem
  sensitive   = true
}


output "rds_host" {
  value       = aws_db_instance.app_rds.address
  sensitive   = true
  description = "RDS host name"
}


output "rds_db_name" {
  value       = aws_db_instance.app_rds.db_name
  sensitive   = true
  description = "RDS database name"
}




