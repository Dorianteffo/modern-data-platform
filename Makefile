tf-init :
	terraform -chdir=./terraform init 

tf-plan: 
	terraform -chdir=./terraform plan 


tf-apply: 
	terraform -chdir=./terraform apply


ec2-private-key: 
	terraform -chdir=./terraform output -raw private_key


ec2-dns: 
	terraform -chdir=./terraform output -raw ec2_public_dns



rds-host: 
	terraform -chdir=./terraform output -raw rds_host


rds-db: 
	terraform -chdir=./terraform output -raw rds_db_name


tf-destroy: 
	terraform -chdir=./terraform destroy



##########################################################################################"

################# Data Generator###########################################

up-ci: 
	cd data_generator && docker compose up --build -d ci

format:
	cd data_generator && docker exec app python -m black -S --line-length 79 .

isort:
	cd data_generator && docker exec app isort .

type:
	cd data_generator && docker exec app mypy --ignore-missing-imports .

lint: 
	cd data_generator && docker exec app flake8 .

ci: isort format type lint

generate-data: 
	cd data_generator && docker compose --env-file .env up --build -d run


down: 
	cd data_generator && docker compose down 


###############################################################################################""
airbyte-ec2: 
	terraform -chdir=./terraform output -raw private_key > private_key.pem && chmod 600 private_key.pem && ssh -o StrictHostKeyChecking=no -o IdentitiesOnly=yes -i private_key.pem ec2-user@$$(terraform -chdir=./terraform output -raw airbyte_ec2_public_dns) && rm private_key.pem




airbyte: 
	terraform -chdir=./terraform output -raw private_key > private_key.pem && chmod 600 private_key.pem && ssh -o "IdentitiesOnly yes" -i private_key.pem ec2-user@$$(terraform -chdir=./terraform output -raw airbyte_ec2_public_dns) -N -f -L 9000:localhost:8000 && rm private_key.pem


