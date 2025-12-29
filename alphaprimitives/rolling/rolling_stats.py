import pandas as pd
import bottleneck as bn

def rolling_var(x: pd.DataFrame, w: int) -> pd.DataFrame:
    out = bn.move_var(x.values, window=w, min_count=1, axis=0)
    return pd.DataFrame(out, index=x.index, columns=x.columns)


def rolling_std(x: pd.DataFrame, w: int) -> pd.DataFrame:
    out = bn.move_std(x.values, window=w, min_count=1, axis=0)
    return pd.DataFrame(out, index=x.index, columns=x.columns)


def rolling_skew(x: pd.DataFrame, w: int) -> pd.DataFrame:
    return x.rolling(window=w, min_periods=1).skew()


def rolling_kurt(x: pd.DataFrame, w: int) -> pd.DataFrame:
    return x.rolling(window=w, min_periods=1).kurt()
