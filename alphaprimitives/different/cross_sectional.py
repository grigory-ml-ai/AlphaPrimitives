import numpy as np
import pandas as pd


def demean_cross_sectional(x: pd.DataFrame) -> pd.DataFrame:
    mean_row = x.mean(axis=1)
    return x.sub(mean_row, axis=0)


def cs_mean(x: pd.DataFrame) -> pd.DataFrame:
    mr = x.mean(axis=1)
    return pd.DataFrame(
        index=x.index,
        columns=x.columns,
        data=np.repeat(mr.values[:, None], x.shape[1], axis=1),
    )


def cs_rank(x: pd.DataFrame) -> pd.DataFrame:
    return x.rank(axis=1, pct=False)


def cs_percentile(x: pd.DataFrame) -> pd.DataFrame:
    return x.rank(axis=1, pct=True)


def cs_zscore(x: pd.DataFrame) -> pd.DataFrame:
    # The Cross-Section of Volatility and Expected Returns (IVOL Puzzle)
    mean_row = x.mean(axis=1)
    std_row = x.std(axis=1, ddof=0) + 1e-8
    return x.sub(mean_row, axis=0).div(std_row, axis=0)


def cs_range_normalize(x: pd.DataFrame) -> pd.DataFrame:
    mn = x.min(axis=1)
    mx = x.max(axis=1)
    return x.sub(mn, axis=0).div(mx - mn, axis=0)


def cs_divergence(x: pd.DataFrame) -> pd.DataFrame:
    mu = x.mean(axis=1)
    return (x.sub(mu, axis=0)) ** 2


def cs_winsorize(x: pd.DataFrame, percentile: float = 0.01) -> pd.DataFrame:
    lo = x.quantile(percentile, axis=1)
    hi = x.quantile(1.0 - percentile, axis=1)
    return x.clip(lower=lo, upper=hi, axis=0)


def cs_resid(x: pd.DataFrame, y: pd.DataFrame) -> pd.DataFrame:
    x_, y_ = x.align(y, join='inner', axis=0)
    x_ = x_.reindex(columns=x.columns)
    y_ = y_.reindex(columns=x.columns)
    X = x_.to_numpy(np.float64, copy=False)
    Y = y_.to_numpy(np.float64, copy=False)
    out = np.full_like(X, np.nan)
    for i in range(X.shape[0]):
        xi = X[i, :]
        yi = Y[i, :]
        mask = np.isfinite(xi) & np.isfinite(yi)
        if mask.sum() < 2:
            continue
        A = yi[mask].reshape(-1, 1)
        b, _, _, _ = np.linalg.lstsq(A, xi[mask], rcond=None)
        res = xi.copy()
        res[mask] = xi[mask] - (A @ b).ravel()
        out[i, :] = res
    return pd.DataFrame(index=x_.index, columns=x_.columns, data=out)
