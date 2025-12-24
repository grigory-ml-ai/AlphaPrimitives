import numpy as np
import pandas as pd
from numba import njit, prange, jit


@jit(cache=True)
def _rolling_nanprod_vec(x: np.ndarray, w: int) -> np.ndarray:
    if w <= 1:
        raise ValueError(f'Error at _rolling_nanprod_vec. Window len must be greater than 1. Got: {w}')
    n = x.size
    out = np.empty(n, dtype=np.float64)
    temp = 1
    for i in range(n):
        temp *= (x[i] if np.isfinite(x[i]) else 1.0)
        if i >= w:
            temp /= (x[i - w] if np.isfinite(x[i - w]) else 1.0)
        out[i] = temp
    return out


@jit(cache=True, parallel=True)
def column_wise_apply(x: np.ndarray, w: int) -> np.ndarray:
    n_rows, n_cols = x.shape
    out = np.empty_like(x, dtype=x.dtype)
    for col in prange(n_cols):
        out[:, col] = _rolling_nanprod_vec(x[:, col], w)
    return out


def rolling_prod(x: pd.DataFrame, w: int) -> pd.DataFrame:
    out = column_wise_apply(x.values, w)
    return pd.DataFrame(out, index=x.index, columns=x.columns)
