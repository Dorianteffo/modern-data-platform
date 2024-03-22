from cosmos.config import ProjectConfig, ProfileConfig, ExecutionConfig, RenderConfig
from cosmos.airflow.task_group import DbtTaskGroup
from cosmos.profiles import SnowflakeUserPasswordProfileMapping
from datetime import datetime 
from airflow.decorators import dag
from cosmos.constants import LoadMode
from airflow.operators.bash_operator import BashOperator

DBT_PROJECT_PATH = "/opt/airflow/dags/dbt/dbt_transformation"
DBT_EXECUTABLE_PATH = "/opt/airflow/dbt_venv/bin/dbt"


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
    schedule_interval="0 20 * * *",  # every day at 20
    start_date=datetime(2024, 3, 22),
    catchup=False,
    tags=["dbt", "snowflake"],
    dag_id='dbt-snowflake-dag'
)
def dataplatfom_dag():

    pre_dbt = BashOperator(
        task_id='pre_dbt',
        bash_command='echo "Pipeline start..."'
    )

    dbt_transform = DbtTaskGroup(
        group_id = "dbt_prod",
        project_config=ProjectConfig(DBT_PROJECT_PATH),
        execution_config = ExecutionConfig(dbt_executable_path = DBT_EXECUTABLE_PATH),
        profile_config=profile_config_prod,
        default_args={"retries": 2},
        render_config=RenderConfig(
            load_method=LoadMode.DBT_LS,
            select=['path:models']
        )
    )

    post_dbt = BashOperator(
        task_id='post_dbt',
        bash_command='echo "Pipeline end..."'
    )

    pre_dbt >> dbt_transform >> post_dbt

dataplatfom_dag()



