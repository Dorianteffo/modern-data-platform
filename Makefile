########################################################################################

###################### Terraform  ########################################
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




##########################################################################################

################# Data Generator ###########################################

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





###############################################################################################

################## DBT #####################################

dbt-up: 
	cd analytics && docker compose --env-file .env up --build -d


dbt-debug: 
	cd analytics && winpty docker exec -it dbt bash -c "cd dbt && dbt debug --profiles-dir=."


dbt-test: 
	cd analytics && winpty docker exec -it dbt bash -c "cd dbt && dbt test --profiles-dir=."


dbt-run: 
	cd analytics && winpty docker exec -it dbt bash -c "cd dbt && dbt run --profiles-dir=."


dbt-deps: 
	cd analytics && winpty docker exec -it dbt bash -c "cd dbt && dbt deps --profiles-dir=."


dbt-deploy: 
	cd analytics && winpty docker exec -it dbt bash -c "cd dbt && dbt run --profiles-dir=. --target prod"



dbt-down: 
	cd analytics && docker compose down

