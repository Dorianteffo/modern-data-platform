import logging

import os
from dataclasses import dataclass

import datetime
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

default_date = datetime(1900, 10, 10, 0, 0, 0)

@dataclass
class DBConnection:
    database: str
    user: str
    pwd: str
    host: str
    port: int


def get_warehouse_creds() -> DBConnection:
    return DBConnection(
        user=os.getenv('POSTGRES_USER', ''),
        pwd=os.getenv('POSTGRES_PASSWORD', ''),
        database=os.getenv('POSTGRES_DB', ''),
        host=os.getenv('POSTGRES_HOST', ''),
        port=int(os.getenv('POSTGRES_PORT', 5432)),
    )


class WarehouseConnection:
    def __init__(self, db_conn: DBConnection):
        self.conn_url = (
            f'postgresql://{db_conn.user}:{db_conn.pwd}@'
            f'{db_conn.host}:{db_conn.port}/{db_conn.database}'
        )


    def connection_string(self):
        return self.conn_url



def create_conn(connection_string : str):
    # connect to the postgres database
    try:
        engine = create_engine(connection_string)
        logger.info("Connected to postgres database!!")
        return engine
    except Exception as e:
        logger.error("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        logger.error(f"Enable to connect to postgres : {e}")



def close_conn(engine : Engine):
    # close the connection
    engine.dispose()



def insert_etl_log(engine : Engine, etl_log_table : str, source_table_name : str, rowcount : int, schema_name : str, error_code : str = 'NA'): 
    try : 
        record = {
            "last_extract_datetime" : datetime.now(), 
            "table_name" : source_table_name,
            "extract_row_count" : rowcount, 
            "error_code": error_code
        }


        etl_log_df = pd.DataFrame(record)
        etl_log_df.to_sql(etl_log_table,engine, if_exists='append', index=False, schema=schema_name)
        logger.info(f"{etl_log_table} table successfully updated!!!!")

    except Exception as e: 
        logger.error("!!!!!!!!!!!!!!!!!!!!")
        logger.error(f"Failed to insert data to {etl_log_table}: {e}")




def gest_last_runtime(engine : Engine, etl_log_table : str, source_table_name : str) : 
    try : 
        sql_query = f"""
            SELECT MAX(last_extract_datetime)
            FROM {etl_log_table}
            WHERE table_name LIKE '{source_table_name}' AND 
            error_code LIKE 'NA'
    """
        etl_log_df = pd.read_sql(sql_query, con=engine)
        last_run_time = etl_log_df['last_extract_datetime'][0]
        if not last_run_time : 
            last_run_time == default_date
            return last_run_time
    
    except Exception: 
        return default_date


def lambda_handler(event, context):

