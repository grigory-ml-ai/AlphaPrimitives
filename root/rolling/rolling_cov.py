import numpy as np
import pandas as pd
from numba import njit, prange


@njit(cache=True, fastmath=False)
def _rolling_cov_vec_numba(x: np.ndarray, y: np.ndarray, window, min_periods=None, ddof=1):
    n = x.shape[0]
    if y.shape[0] != n:
        raise ValueError("x and y must have the same length")
    if window <= 0:
        raise ValueError("window must be positive")
    if min_periods is None:
        min_periods = window
    if min_periods <= 0:
        min_periods = 1

    out = np.empty(n, dtype=np.float64)
    out[:] = np.nan

    sX = 0.0
    sY = 0.0
    sXY = 0.0
    cnt = 0

    # Работаем с окнами по индексу i, текущее окно: [i-window+1, i]
    for i in range(n):
        xi = x[i]
        yi = y[i]

        # Добавляем текущую точку, если она не NaN
        if not (np.isnan(xi) or np.isnan(yi)):
            sX += xi
            sY += yi
            sXY += xi * yi
            cnt += 1

        # Удаляем ушедший элемент (i - window)
        j = i - window
        if j >= 0:
            xj = x[j]
            yj = y[j]
            if not (np.isnan(xj) or np.isnan(yj)):
                sX -= xj
                sY -= yj
                sXY -= xj * yj
                cnt -= 1

        # Число фактически валидных точек в текущем окне
        k = cnt

        # Условие вывода ковариации
        if k >= min_periods and k > ddof:
            # ковариация: E[XY] - E[X]E[Y]
            meanX = sX / k
            meanY = sY / k
            cov = (sXY - k * meanX * meanY) / (k - ddof)
            out[i] = cov
        else:
            out[i] = np.nan

    return out


@njit(cache=True, parallel=True)
def column_wise_apply(x: np.ndarray, w: int) -> np.ndarray:
    n_rows, n_cols = x.shape
    out = np.empty_like(x, dtype=x.dtype)
    for col in prange(n_cols):
        out[:, col] = _rolling_cov_vec_numba(x[:, col], w)
    return out


def rolling_cov(x: pd.DataFrame, w: int) -> pd.DataFrame:
    out = column_wise_apply(x.values, w)
    return pd.DataFrame(out, index=x.index, columns=x.columns)
