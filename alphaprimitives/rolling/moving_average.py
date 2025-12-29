import bottleneck as bn
import numpy as np
import pandas as pd
from numba import prange, njit
from numpy.lib.stride_tricks import sliding_window_view
from scipy.signal import savgol_filter


def sma(x: pd.DataFrame, w: int) -> pd.DataFrame:
    if w <= 1:
        raise ValueError(f'Error at sma. Window len must be greater than 1. Got: {w}')
    out = bn.move_mean(x.values, window=w, min_count=1, axis=0)
    return pd.DataFrame(out, index=x.index, columns=x.columns)


def ema(x: pd.DataFrame, alpha: float) -> pd.DataFrame:
    if not 0 < alpha < 1:
        raise ValueError(f'Error at ema. Alpha must be a value in (0, 1). Got: {alpha}')
    return x.ewm(alpha=alpha, min_periods=1).mean()


def rolling_median(x: pd.DataFrame, w: int) -> pd.DataFrame:
    if w <= 1:
        raise ValueError(f'Error at rolling_median. Window len must be greater than 1. Got: {w}')
    out = bn.move_median(x.values, window=w, min_count=1, axis=0)
    return pd.DataFrame(out, index=x.index, columns=x.columns)


def savgol_smoothing(x: pd.DataFrame, w: int = 3, polyorder: int = 3) -> pd.DataFrame:
    y = savgol_filter(x=x, window_length=w, polyorder=polyorder, axis=0)
    return pd.DataFrame(data=y, index=x.index, columns=x.columns)


@njit(nopython=True, cache=True)
def _wma_vec_numba(x: np.ndarray, w: int) -> np.ndarray:
    if w <= 1:
        raise ValueError(f'Error at wma_numba. Window len must be greater than 1. Got: {w}')
    window = np.divide(np.arange(1, w + 1), 5).reshape(-1, 1)
    x = sliding_window_view(x, window_shape=w)
    x = np.where(np.isfinite(x), x, 0)
    return (x @ window).ravel()


def wma(x: pd.DataFrame, w: int) -> pd.DataFrame:
    @njit(cache=True, parallel=True)
    def _column_wise_apply(x: np.ndarray, w: int) -> np.ndarray:
        n_rows, n_cols = x.shape
        out = np.empty_like(x, dtype=x.dtype)
        for col in prange(n_cols):
            out[:, col] = _wma_vec_numba(x[:, col], w)
        return out

    return pd.DataFrame(_column_wise_apply(x.values, w), index=x.index, columns=x.columns)


def hull_moving_average(x: pd.DataFrame, w: int) -> pd.DataFrame:
    if w <= 4:
        raise ValueError(f'Error at hull_moving_average. Window len must be greater than 1. Got: {w}')
    wma_raw = 2 * wma(x, w) - wma(x, w // 2)
    return wma(wma_raw, int(np.sqrt(w)))
