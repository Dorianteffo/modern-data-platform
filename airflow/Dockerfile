FROM apache/airflow:2.8.3

COPY requirements.txt /

RUN pip install apache-airflow==${AIRFLOW_VERSION} astronomer-cosmos

# Install virtualenv
RUN pip install virtualenv

# Create a writable directory for the virtual environment
RUN mkdir -p /opt/airflow/dbt_venv

# Create the virtual environment using virtualenv
RUN virtualenv /opt/airflow/dbt_venv
RUN /opt/airflow/dbt_venv/bin/pip install dbt-snowflake


# RUN python -m venv dbt_venv && source dbt_venv/bin/activate && \
#     pip install --no-cache-dir dbt-snowflake && deactivate