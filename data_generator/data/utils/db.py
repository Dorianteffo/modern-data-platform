import os
from dataclasses import dataclass


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
