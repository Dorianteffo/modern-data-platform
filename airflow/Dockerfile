FROM apache/airflow:2.8.3

COPY requirements.txt /

RUN pip install apache-airflow==${AIRFLOW_VERSION} astronomer-cosmos

# Create the virtual environment using virtualenv
RUN python -m venv dbt_venv

# Activate the virtual environment
RUN source dbt_venv/bin/activate && \
    pip install --no-cache-dir --ignore-installed dbt-snowflake && \
    deactivate
