import numpy as np
import pandas as pd


def power(x: pd.DataFrame, v: float) -> pd.DataFrame:
    return x.pow(v)


def log1p(x: pd.DataFrame) -> pd.DataFrame:
    return x.apply(np.log1p)


def abs(x: pd.DataFrame) -> pd.DataFrame:
    return x.abs()


def sigmoid(x: pd.DataFrame) -> pd.DataFrame:
    data = np.divide(1, 1 + np.exp(-x.values))
    return pd.DataFrame(data=data, index=x.index, columns=x.columns)


def tanh(x: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(data=np.tanh(x.values), index=x.index, columns=x.columns)


def relu(x: pd.DataFrame) -> pd.DataFrame:
    data = np.where(x.values > 0, x.values, 0)
    return pd.DataFrame(data=data, index=x.index, columns=x.columns)


