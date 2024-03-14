import logging

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


def create_conn(connection_string: str):
    # connect to the postgres database
    try:
        engine = create_engine(connection_string)
        logger.info("Connected to postgres database!!")
        return engine
    except Exception as e:
        logger.error("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        logger.error(f"Enable to connect to postgres : {e}")


def load_table(
    df: pd.DataFrame,
    engine: Engine,
    table_name: str,
    schema_name: str,
    load_mode: str,
):
    try:
        df.to_sql(
            table_name,
            engine,
            if_exists=load_mode,
            index=False,
            schema=schema_name,
        )
        logger.info(
            f"Table {table_name} loaded to the {schema_name} schema!!!"
        )
    except Exception as e:
        logger.error("!!!!!!!!!!!!!!!!!!!!!!")
        logger.error(
            f"Enable to load {table_name} to {schema_name} schema : {e}"
        )


def close_conn(engine: Engine):
    # close the connection
    engine.dispose()
