import numpy as np
import pandas as pd
from numba import njit, prange


@njit(cache=True)
def _rolling_quadratic_variation_vec_numba(x: np.ndarray, w: int) -> np.ndarray:
    assert w > 1, f'Error at rolling_quadratic_variation. window size must be greater then 1. Got: {w}'
    n = x.shape[0]
    out = np.full(n, np.nan, dtype=np.float64)

    if n == 0:
        return out
    buf = np.full(w, np.nan, dtype=np.float64)

    rsum = 0.0
    valid_count = 0
    for i in range(1, n):
        val = x[i]
        prev = x[i - 1]
        if np.isnan(val) or np.isnan(prev):
            sq = np.nan
        else:
            diff = val - prev
            sq = diff * diff

        if not np.isnan(sq):
            rsum += sq
            valid_count += 1

        if i >= w:
            old_sq = buf[i % w]
            if not np.isnan(old_sq):
                rsum -= old_sq
                valid_count -= 1

        buf[i % w] = sq

        if valid_count >= 1:
            out[i] = rsum

    return out


def rolling_quadratic_variation(x: pd.DataFrame, w: int) -> pd.DataFrame:
    assert w > 1, f'Error at rolling_quadratic_variation. window size must be greater then 1. Got: {w}'

    @njit(cache=True, parallel=True)
    def column_wise_apply(x: np.ndarray, w: int) -> np.ndarray:
        n_rows, n_cols = x.shape
        out = np.empty_like(x, dtype=x.dtype)
        for col in prange(n_cols):
            out[:, col] = _rolling_quadratic_variation_vec_numba(x[:, col], w)
        return out

    return pd.DataFrame(column_wise_apply(x.values, w), index=x.index, columns=x.columns)
