import os
from concurrent.futures import ThreadPoolExecutor
from fractions import Fraction
from pathlib import Path

import pandas as pd
from sqlalchemy import (
    Column, Integer, String, Text, Boolean, DateTime,
    CheckConstraint, UniqueConstraint, ForeignKey, Numeric,
    BigInteger
)
from sqlalchemy import text
from sqlalchemy.orm import declarative_base

from alphaprimitives.sql.connection import ConnectionPostgres
from tqdm import tqdm
Base = declarative_base()



class Operator(Base):
    __tablename__ = "operators"
    __table_args__ = (
        UniqueConstraint("operator_name", "version", name="uq_operators_name_version"),
        CheckConstraint(r"version ~ '^\d+\.\d+\.\d+$'", name="ck_operators_version_semver"),
    )

    operator_id = Column(Integer, primary_key=True)
    operator_name = Column(String(255), nullable=False)
    version = Column(String(54))
    arity = Column(Integer, nullable=False)
    category = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=text("now()"))
    updated_at = Column(DateTime(timezone=True), nullable=False, server_default=text("now()"))
    description = Column(Text)
    commutative = Column(Boolean)
    associative = Column(Boolean)
    idempotent = Column(Boolean)


class OperatorArg(Base):
    __tablename__ = "operator_args"
    __table_args__ = (
        UniqueConstraint("operator_id", "position", name="uq_operator_args_operator_position"),
    )

    arg_id = Column(Integer, primary_key=True)  # serial not null -> PK
    operator_id = Column(
        Integer,
        ForeignKey("operators.operator_id", ondelete="CASCADE"),
        nullable=False
    )
    position = Column(Integer, nullable=False)
    arg_name = Column(String(64), nullable=False)
    kind = Column(String(64), nullable=False)
    can_be_register = Column(Boolean, nullable=False)
    min_value = Column(Numeric)
    max_value = Column(Numeric)


class Feature(Base):
    __tablename__ = "feature_pool"
    feature_id = Column(Integer, primary_key=True)
    value = Column(String(255), nullable=False)
    dimension = Column(String(255), nullable=False)


class Window(Base):
    __tablename__ = "window_pool"
    window_id = Column(Integer, primary_key=True)
    value = Column(Integer, nullable=False)


class Scalar(Base):
    __tablename__ = "scalar_pool"
    scalar_id = Column(Integer, primary_key=True)
    value = Column(Numeric, nullable=False)


class Futures(Base):
    __tablename__ = 'futures'

    open_time = Column(DateTime(timezone=True), nullable=False, primary_key=True)
    ticker_name = Column(String(20), nullable=False, primary_key=True)
    open = Column(Numeric(20, 10), nullable=True)
    high = Column(Numeric(20, 10), nullable=True)
    low = Column(Numeric(20, 10), nullable=True)
    close = Column(Numeric(20, 10), nullable=True)
    volume = Column(Numeric(30, 8), nullable=True)
    close_time = Column(DateTime(timezone=True), nullable=True)
    quote_volume = Column(Numeric(30, 8), nullable=True)
    count = Column(BigInteger, nullable=True)
    taker_buy_volume = Column(Numeric(30, 8), nullable=True)
    taker_buy_quote_volume = Column(Numeric(30, 8), nullable=True)

def push_operators(connection: ConnectionPostgres, reset: bool = True) -> None:
    if reset:
        connection.reset('operators')
    connection.push(pd.read_json('operators.json'), table_name='operators')


def push_operator_args(connection: ConnectionPostgres, reset: bool = True) -> None:
    if reset:
        connection.reset('operator_args')

    df_operators = connection.fetch('operators', columns=['operator_id', 'operator_name'])
    df_operator_args: pd.DataFrame = (
        pd.read_json('operator_args.json')
        .merge(df_operators, on='operator_name', how='left')
        .drop(columns=['operator_name'])
    )
    connection.push(df_operator_args, table_name='operator_args')


def push_feature_pool(connection: ConnectionPostgres, reset: bool = True) -> None:
    if reset:
        connection.reset('feature_pool')
    connection.push(pd.read_json('feature_pool.json'), table_name='feature_pool')


def push_window_pool(connection: ConnectionPostgres, reset: bool = True) -> None:
    if reset:
        connection.reset('window_pool')


    WINDOW_POOL = [
        3, 5, 6, 8, 10, 12, 14, 15, 18, 20,
        24, 26, 30, 36, 40, 48, 50, 52, 60,
        65, 72, 78, 104, 130, 156, 195, 234,
        260, 312, 390
    ]
    df_window_pool = pd.Series(
        data=WINDOW_POOL,
        name='value'
    ).to_frame()
    connection.push(df_window_pool, table_name='window_pool')


def push_scalar_pool(connection: ConnectionPostgres, reset: bool = True) -> None:
    if reset:
        connection.reset('scalar_pool')
    SCALAR_POOL = [
        Fraction(-4, 1), Fraction(-47, 12), Fraction(-23, 6), Fraction(-15, 4),
        Fraction(-11, 3), Fraction(-43, 12), Fraction(-7, 2), Fraction(-41, 12),
        Fraction(-10, 3), Fraction(-13, 4), Fraction(-19, 6), Fraction(-37, 12),
        Fraction(-3, 1), Fraction(-35, 12), Fraction(-17, 6), Fraction(-11, 4),
        Fraction(-8, 3), Fraction(-31, 12), Fraction(-5, 2), Fraction(-29, 12),
        Fraction(-7, 3), Fraction(-9, 4), Fraction(-13, 6), Fraction(-25, 12),
        Fraction(-2, 1), Fraction(-23, 12), Fraction(-11, 6), Fraction(-7, 4),
        Fraction(-5, 3), Fraction(-19, 12), Fraction(-3, 2), Fraction(-17, 12),
        Fraction(-4, 3), Fraction(-5, 4), Fraction(-7, 6), Fraction(-13, 12),
        Fraction(-1, 1), Fraction(-11, 12), Fraction(-5, 6), Fraction(-3, 4),
        Fraction(-2, 3), Fraction(-7, 12), Fraction(-1, 2), Fraction(-5, 12),
        Fraction(-1, 3), Fraction(-1, 4), Fraction(-1, 6), Fraction(-1, 12),
        Fraction(0, 1), Fraction(1, 12), Fraction(1, 6), Fraction(1, 4),
        Fraction(1, 3), Fraction(5, 12), Fraction(1, 2), Fraction(7, 12),
        Fraction(2, 3), Fraction(3, 4), Fraction(5, 6), Fraction(11, 12),
        Fraction(1, 1), Fraction(13, 12), Fraction(7, 6), Fraction(5, 4),
        Fraction(4, 3), Fraction(17, 12), Fraction(3, 2), Fraction(19, 12),
        Fraction(5, 3), Fraction(7, 4), Fraction(11, 6), Fraction(23, 12),
        Fraction(2, 1), Fraction(25, 12), Fraction(13, 6), Fraction(9, 4),
        Fraction(7, 3), Fraction(29, 12), Fraction(5, 2), Fraction(31, 12),
        Fraction(8, 3), Fraction(11, 4), Fraction(17, 6), Fraction(35, 12),
        Fraction(3, 1), Fraction(37, 12), Fraction(19, 6), Fraction(13, 4),
        Fraction(10, 3), Fraction(41, 12), Fraction(7, 2), Fraction(43, 12),
        Fraction(11, 3), Fraction(15, 4), Fraction(23, 6), Fraction(47, 12),
        Fraction(4, 1)
    ]
    SCALAR_POOL = list(map(float, SCALAR_POOL))

    df_scalar_pool = pd.Series(
        data=SCALAR_POOL,
        name='value'
    ).to_frame()
    connection.push(df_scalar_pool, table_name='scalar_pool')


def download_ticker(connection: ConnectionPostgres, filepath: Path) -> None:
    try:
        df = pd.read_parquet(filepath).drop(columns=['ignore'])
        df['open_time'] = pd.to_datetime(df['open_time'], unit='ms')
        df['close_time'] = pd.to_datetime(df['close_time'], unit='ms')
        df['ticker_name'] = filepath.name.split('-')[0]
        connection.push(df, table_name='futures')
    except Exception as e:
        print(e)


#TODO: Выгрузить тикеры в базу при необходимости
def push_futures(connection: ConnectionPostgres, folder: Path, reset: bool = False) -> None:
    if reset:
        connection.reset('futures')

    ticker_names = connection.fetch("SELECT DISTINCT TICKER_NAME FROM FUTURES")
    ticker_names = [] if ticker_names.empty else ticker_names['ticker_name'].tolist()

    filepaths = [path for path in folder.glob('*.parquet')]
    for filepath in tqdm(filepaths, total=len(filepaths)):
        if filepath.name.split('-')[0] not in ticker_names:
            download_ticker(connection, filepath)


def main():

    with ConnectionPostgres() as conn:
        conn.create_all(Base)

        # push_operators(conn, reset=True)
        # push_operator_args(conn, reset=True)
        # push_feature_pool(conn, reset=True)
        # push_window_pool(conn, reset=True)
        # push_scalar_pool(conn, reset=True)
        push_futures(conn, folder=Path(r'C:\Users\LianLi\Desktop\trading'), reset=True)


if __name__ == "__main__":
    main()
