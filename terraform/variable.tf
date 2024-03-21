variable "database_name" {
  type        = string
  default     = "application"
  description = "RDS postgres database name"
}


variable "instance_type" {
  type        = string
  default     = "t2.micro"
  description = "Instance type for EC2"
}


variable "key_name" {
  type        = string
  default     = "app-key"
  description = "EC2 key name"
}

variable "username_db" {
  type        = string
  default     = "dorian"
  description = "Username rds"
}

variable "pwd_db" {
  type        = string
  default     = "12345"
  description = "Password rds"
}


variable "airflow_instance_type" {
  type        = string
  default     = "t2.xlarge"
  description = "Airflow instance typ ec2"
}






