## Setup 

* Before running the terraform apply 
export TF_VAR_pwd_db=your_db_password

* Snowflake structure 
```  
RAW  : database to store raw data coming from Airbyte (schemas : postgres_airbyte )
ANALYTICS : the production data (schemas: staging, intermediate, marts(finance))
DBT_DEV: the dev database (the same schemas as the production database)

```

* Ingest data (daily) from RDS to Snowflake : Airbyte




