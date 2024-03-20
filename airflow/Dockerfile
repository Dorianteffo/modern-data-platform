FROM apache/airflow:2.8.3

COPY requirements.txt /

RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" -r /requirements.txt

# Install dbt-snowflake inside a virtual environment
RUN python -m venv /opt/airflow/dbt_venv && \
    . /opt/airflow/dbt_venv/bin/activate && \
    pip install --no-cache-dir --prefix=/opt/airflow/dbt_venv dbt-snowflake && \
    deactivate

USER airflow