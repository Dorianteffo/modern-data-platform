## Setup 

* Before running the terraform apply 
export TF_VAR_pwd_db=your_db_password

* Snowflake structure 
```  
RAW  : database to store raw data coming from Airbyte (schemas : postgres_airbyte )
ANALYTICS : the production data (schemas: staging, intermediate, marts(finance))
DBT_DEV: the dev database (the same schemas as the production database)

DATA_ENGINEER : A role to allow usage of RAW database and ownership of ANALYTICS AND DBT_DEV
AIRBYTE_ROLE : used by airbyte to write in the RAW database (postgres_airbyte schema)

```

* Ingest data (daily) from RDS to Snowflake : Airbyte

* DBT structure 




