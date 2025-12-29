import bottleneck as bn
import pandas as pd


def rolling_max(x: pd.DataFrame, w: int) -> pd.DataFrame:
    out = bn.move_max(x.values, window=w, min_count=1, axis=0)
    return pd.DataFrame(out, index=x.index, columns=x.columns)


def rolling_min(x: pd.DataFrame, w: int) -> pd.DataFrame:
    out = bn.move_min(x.values, window=w, min_count=1, axis=0)
    return pd.DataFrame(out, index=x.index, columns=x.columns)


def rolling_rank(x: pd.DataFrame, w: int) -> pd.DataFrame:
    out = bn.move_rank(x.values, window=w, min_count=1, axis=0)
    return pd.DataFrame(out, index=x.index, columns=x.columns)


def rolling_argmin(x: pd.DataFrame, w: int) -> pd.DataFrame:
    out = bn.move_argmin(x.values, window=w, min_count=1, axis=0)
    return pd.DataFrame(out, index=x.index, columns=x.columns)


def rolling_argmax(x: pd.DataFrame, w: int) -> pd.DataFrame:
    out = bn.move_argmax(x.values, window=w, min_count=1, axis=0)
    return pd.DataFrame(out, index=x.index, columns=x.columns)


def rolling_quantile(x: pd.DataFrame, w: int) -> pd.DataFrame:
    return x.rolling(w).quantile()


def rolling_deviance(x: pd.DataFrame, w: int) -> pd.DataFrame:
    rolling_max = bn.move_max(x.values, window=w, min_count=1, axis=0)
    rolling_min = bn.move_min(x.values, window=w, min_count=1, axis=0)
    return pd.DataFrame(rolling_max - rolling_min, index=x.index, columns=x.columns)
