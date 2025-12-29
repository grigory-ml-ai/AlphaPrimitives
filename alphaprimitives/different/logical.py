import pandas as pd


def greater_than(x: pd.DataFrame, y: pd.DataFrame) -> pd.DataFrame:
    return (x > y).astype(float)


def greater_equal(x: pd.DataFrame, y: pd.DataFrame) -> pd.DataFrame:
    return (x >= y).astype(float)


def lower_than(x: pd.DataFrame, y: pd.DataFrame) -> pd.DataFrame:
    return (x < y).astype(float)


def lower_equal(x: pd.DataFrame, y: pd.DataFrame) -> pd.DataFrame:
    return (x <= y).astype(float)


def equal(x: pd.DataFrame, y: pd.DataFrame) -> pd.DataFrame:
    return (x == y).astype(float)


def not_equal(x: pd.DataFrame, y: pd.DataFrame) -> pd.DataFrame:
    return (x != y).astype(float)

