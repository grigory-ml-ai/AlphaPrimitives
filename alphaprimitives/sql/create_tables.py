import pandas as pd
from sqlalchemy import (
    Column, Integer, String, Text, Boolean, DateTime,
    CheckConstraint, UniqueConstraint, ForeignKey, Numeric
)
from sqlalchemy.orm import declarative_base

from alphaprimitives.sql.connection import ConnectionPostgres

Base = declarative_base()

from sqlalchemy import text


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


def create_tables(connection: ConnectionPostgres, reset: bool = False):
    engine = connection.initialize_engine()
    if reset:
        Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def upload_operators(connection: ConnectionPostgres) -> None:
    connection.upload_df_to_db(pd.read_json('operators.json'), table_name='operators')


def upload_operator_args(connection: ConnectionPostgres) -> None:
    df_operators = connection.load_table('operators', columns=['operator_id', 'operator_name'])
    df_operator_args: pd.DataFrame = (
        pd.read_json('operator_args.json')
        .merge(df_operators, on='operator_name', how='left')
        .drop(columns=['operator_name'])
    )
    connection.upload_df_to_db(df_operator_args, table_name='operator_args')


def upload_feature_pool(connection: ConnectionPostgres) -> None:
    connection.upload_df_to_db(pd.read_json('feature_pool.json'), table_name='feature_pool')


def upload_window_pool(connection: ConnectionPostgres) -> None:
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
    connection.upload_df_to_db(df_window_pool, table_name='window_pool')


def upload_scalar_pool(connection: ConnectionPostgres) -> None:
    SCALAR_POOL = [
        -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.25,
        3.5, 3.75, -0.667, -1.833, -3.833, -3.583, -3.333, -3.083, 0.417, 0.667, 0.917, 1.167, -2.833,
        -2.583, -2.333, -2.083, -1.583, -0.583, -0.333, -0.083, 1.417, 1.667, 1.917, 2.167, 2.417, 2.667,
        2.917, 3.167, 3.417, 3.667, 3.917, -2.417, -1.917, -1.667, -1.417, -3.917, -3.667, -3.417, -0.417,
        0.083, 0.333, 0.583, 1.583, -3.167, -2.917, -2.667, -2.167, -1.167, -0.167, 0.833, 1.083, 1.333,
        1.833, 2.083, 2.333, 2.583, 2.833, 3.083, 3.333, 3.583, 3.833, -3.5, -1.75, -3.0, -3.75, -1.333,
        -1.083, -0.833, 0.167, -2.25, -2.0, -1.0, -0.917, -1.5, -2.5, -3.25, -2.75, -1.25
    ]

    df_scalar_pool = pd.Series(
        data=SCALAR_POOL,
        name='value'
    ).to_frame()
    connection.upload_df_to_db(df_scalar_pool, table_name='scalar_pool')


def main(reset: bool = False):
    connection = ConnectionPostgres()
    create_tables(connection, reset)
    upload_operators(connection)
    upload_operator_args(connection)
    upload_feature_pool(connection)
    upload_window_pool(connection)
    upload_scalar_pool(connection)


if __name__ == "__main__":
    main(reset=True)
