from cosmos import DbtTaskGroup, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping
import os
from datetime import datetime 
from airflow.decorators import dag

DBT_PROJECT_PATH = "/opt/airflow/dags/dbt/dbt_transformation"
DBT_EXECUTABLE_PATH = "/opt/airflow/dbt_venv/Lib/site-packages"

profile_config_dev = ProfileConfig(
    profile_name="modern_warehouse",
    target_name="dev",
    profile_mapping= SnowflakeUserPasswordProfileMapping(
        conn_id="snowflake_conn",
        profile_args={"database": "DBT_DEV", "schema": "staging"},
    ),
)


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
        operator_args={"install_deps": True},
        execution_config = ExecutionConfig(dbt_executable_path = DBT_EXECUTABLE_PATH),
        profile_config=profile_config_dev,
        default_args={"retries": 2}
    )


    transform_prod = DbtTaskGroup(
        group_id = "dbt_prod",
        project_config=ProjectConfig(DBT_PROJECT_PATH),
        operator_args={"install_deps": True},
        execution_config = ExecutionConfig(dbt_executable_path = DBT_EXECUTABLE_PATH),
        profile_config=profile_config_prod,
        default_args={"retries": 2}
    )


    transform_dev >> transform_prod

dbt_dag()



