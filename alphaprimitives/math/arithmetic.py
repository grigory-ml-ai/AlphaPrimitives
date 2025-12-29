import numpy as np
import pandas as pd


def add(x: pd.DataFrame, y: pd.DataFrame) -> pd.DataFrame:
    return x + y


def sub(x: pd.DataFrame, y: pd.DataFrame) -> pd.DataFrame:
    return x - y


def mul(x: pd.DataFrame, y: pd.DataFrame) -> pd.DataFrame:
    return x * y


def div(x: pd.DataFrame, y: pd.DataFrame) -> pd.DataFrame:
    return x / y.replace(0, np.nan)
