FROM apache/airflow:2.8.3

COPY requirements.txt /

RUN pip install --no-cache-dir apache-airflow==${AIRFLOW_VERSION} -r /requirements.txt

# install dbt-snowflake in a virtual env
RUN export PIP_USER=false && python -m venv dbt_venv && source dbt_venv/bin/activate && \
    pip install --no-cache-dir --ignore-installed dbt-snowflake && \
    deactivate
