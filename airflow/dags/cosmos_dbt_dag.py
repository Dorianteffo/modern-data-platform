from cosmos.config import ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.airflow.task_group import DbtTaskGroup
from cosmos.profiles import SnowflakeUserPasswordProfileMapping
from datetime import datetime 
from airflow.decorators import dag

DBT_PROJECT_PATH = "/opt/airflow/dags/dbt/dbt_transformation"
DBT_EXECUTABLE_PATH = "/opt/airflow/dbt_venv/bin/dbt"

# dev environment 
profile_config_dev = ProfileConfig(
    profile_name="modern_warehouse",
    target_name="dev",
    profile_mapping= SnowflakeUserPasswordProfileMapping(
        conn_id="snowflake_conn",
        profile_args={"database": "DBT_DEV", "schema": "staging"},
    ),
)


# profile for the prod env
profile_config_prod = ProfileConfig(
    profile_name="modern_warehouse",
    target_name="prod",
    profile_mapping= SnowflakeUserPasswordProfileMapping(
        conn_id="snowflake_conn",
        profile_args={"database": "ANALYTICS", "schema": "staging"},
    ),
)

@dag(
    schedule_interval="@daily",
    start_date=datetime(2024, 3, 20),
    catchup=False,
    tags=["dbt", "snowflake"],
    dag_id='dbt-snowflake-dag'
)
def dbt_dag():
    transform_dev = DbtTaskGroup(
        group_id = "dbt_dev",
        project_config=ProjectConfig(DBT_PROJECT_PATH),
        execution_config = ExecutionConfig(dbt_executable_path = DBT_EXECUTABLE_PATH),
        profile_config=profile_config_dev,
        default_args={"retries": 2}
    )


    transform_prod = DbtTaskGroup(
        group_id = "dbt_prod",
        project_config=ProjectConfig(DBT_PROJECT_PATH),
        execution_config = ExecutionConfig(dbt_executable_path = DBT_EXECUTABLE_PATH),
        profile_config=profile_config_prod,
        default_args={"retries": 2}
    )


    transform_dev >> transform_prod

dbt_dag()



