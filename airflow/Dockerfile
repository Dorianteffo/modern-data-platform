FROM apache/airflow:2.8.0

COPY requirements.txt /

RUN pip install apache-airflow==${AIRFLOW_VERSION} astronomer-cosmos

RUN python -m venv dbt_venv && source dbt_venv/bin/activate && \
    pip install --no-cache-dir dbt-snowflake && deactivate