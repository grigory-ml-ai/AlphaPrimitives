import numpy as np
import pandas as pd
from numba import njit, prange


@njit(cache=True, fastmath=False, nogil=True)
def _rolling_sum_vec_numba(x: np.ndarray, w: int) -> np.ndarray:
    n = x.size
    out = np.empty(n, dtype=x.dtype)

    current_sum = 0.0
    valid_count = 0

    for i in range(n):
        val = x[i]
        if not np.isnan(val):
            current_sum += val
            valid_count += 1
        if i >= w:
            old_val = x[i - w]
            if not np.isnan(old_val):
                current_sum -= old_val
                valid_count -= 1
        if valid_count > 0:
            out[i] = current_sum
        else:
            out[i] = np.nan

    return out


@njit(cache=True, parallel=True)
def column_wise_apply(x: np.ndarray, w: int) -> np.ndarray:
    n_rows, n_cols = x.shape
    out = np.empty_like(x, dtype=x.dtype)
    for col in prange(n_cols):
        out[:, col] = _rolling_sum_vec_numba(x[:, col], w)
    return out


def rolling_sum(x: pd.DataFrame, w: int) -> pd.DataFrame:
    out = column_wise_apply(x.values, w)
    return pd.DataFrame(out, index=x.index, columns=x.columns)
