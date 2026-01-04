from typing import List, Optional

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine


class ConnectionPostgres:
    def __init__(self,
                 login: str = 'postgres',
                 password: str = 'password',
                 host: str = 'localhost',
                 port: int = '5432',
                 db_name: str = 'postgres'):
        self._login = login
        self._db_name = db_name
        self._password = password
        self._host = host
        self._port = port
        self._connection_string = self._initialize_connection_string()

    def _initialize_connection_string(self) -> str:
        return 'postgresql://{login}:{password}@{host}:{port}/{db_name}'.format(
            login=self._login,
            password=self._password,
            host=self._host,
            port=self._port,
            db_name=self._db_name
        )

    def initialize_engine(self) -> Engine:
        return create_engine(self._connection_string)

    def load_table(self, table: str, columns: Optional[List[str]] = None) -> pd.DataFrame:
        return pd.read_sql_table(table, self.initialize_engine(), columns=columns)

    def upload_df_to_db(self, df: pd.DataFrame, table_name: str) -> None:
        df.to_sql(name=table_name, con=self.initialize_engine(), if_exists='append', index=False)






