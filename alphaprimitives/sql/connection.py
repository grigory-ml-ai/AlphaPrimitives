from typing import List, Optional

import pandas as pd
from sqlalchemy import create_engine, text, inspect
from sqlalchemy.engine.base import Engine
from multipledispatch import dispatch
from sqlalchemy.orm import DeclarativeMeta, DeclarativeBase


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
        self._engine = self._initialize_engine()

    def _initialize_engine(self) -> Engine:
        connection_string = self._initialize_connection_string()
        return create_engine(connection_string)

    def _initialize_connection_string(self) -> str:
        return 'postgresql://{login}:{password}@{host}:{port}/{db_name}'.format(
            login=self._login,
            password=self._password,
            host=self._host,
            port=self._port,
            db_name=self._db_name
        )

    def __enter__(self):
        self._engine.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._engine.dispose()

    @dispatch(str, list)
    def fetch(self, table: str, columns: Optional[List[str]] = None) -> pd.DataFrame:
        return pd.read_sql_table(table, self._engine, columns=columns)

    def push(self, df: pd.DataFrame, table_name: str) -> None:
        df.to_sql(name=table_name,
                  con=self._engine,
                  if_exists='append',
                  index=False,
                  method='multi',
                  chunksize=10000
                  )

    @dispatch(str)
    def fetch(self, sql_string: str) -> Optional[pd.DataFrame]:
        return pd.read_sql(sql=sql_string, con=self._engine)

    def drop(self, table_name: str) -> None:
        with self._engine.connect() as conn:
            conn.execute(text(f"DROP TABLE IF EXISTS {table_name} CASCADE"))
            conn.commit()

    def reset(self, table_name: str) -> None:
        with self._engine.connect() as conn:
            conn.execute(text(f'TRUNCATE TABLE "{table_name}" RESTART IDENTITY CASCADE'))
            conn.commit()


    def exists(self, table_name: str) -> bool:
        return inspect(self._engine).has_table(table_name)

    def create_all(self, Base: type[DeclarativeBase]) -> None:
        Base.metadata.create_all(self._engine)






