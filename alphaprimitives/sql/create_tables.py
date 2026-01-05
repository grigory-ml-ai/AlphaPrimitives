import pandas as pd
from sqlalchemy import (
    Column, Integer, String, Text, Boolean, DateTime,
    CheckConstraint, UniqueConstraint, ForeignKey, Numeric
)
from sqlalchemy.orm import declarative_base

from alphaprimitives.sql.connection import ConnectionPostgres
from fractions import Fraction

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
