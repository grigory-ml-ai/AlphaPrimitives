import numpy as np
import pandas as pd
from root.rolling.rolling_corr import _rolling_corr_vec_numba
from kernels import _rolling_cov_vec_numba
from kernels import _rolling_nanprod_vec
from root.rolling.rolling_sum import _rolling_sum_vec_numba
from kernels import _rolling_quadratic_variation_vec_numba


def generate_vector(n=1000) -> pd.Series:
    x = np.where(
        np.random.uniform(0, 1, size=n) < 0.1,
        np.nan,
        np.random.normal(0, 1, size=n)
    )
    return pd.Series(x)


def generate_nan_only() -> pd.Series:
    return pd.Series([np.nan] * 5)


def generate_one_elem() -> pd.Series:
    return pd.Series([1])


def generate_matrix(n=1000, m=10) -> pd.DataFrame:
    x = np.where(
        np.random.uniform(0, 1, size=(n, m)) < 0.1,
        np.nan,
        np.random.normal(0, 1, size=(n, m))
    )
    return pd.DataFrame(x)


def test_rolling_corr():
    x = generate_vector()
    y = generate_vector()
    w = 5
    v1 = x.rolling(min_periods=1, window=w).corr(y).to_numpy()
    v2 = _rolling_corr_vec_numba(x.to_numpy(), y.to_numpy(), window=w, min_periods=1)
    assert np.allclose(v1, v2, equal_nan=True)


def test_rolling_cov():
    x = generate_vector()
    y = generate_vector()
    w = 5
    v1 = x.rolling(min_periods=1, window=w).cov(y).to_numpy()
    v2 = _rolling_cov_vec_numba(x.to_numpy(), y.to_numpy(), window=w, min_periods=1)
    assert np.allclose(v1, v2, equal_nan=True)


def test_rolling_prod_vec():
    x = generate_vector()
    w = 5
    v1 = x.rolling(min_periods=1, window=w).apply(np.nanprod).to_numpy()
    v2 = _rolling_nanprod_vec(x.to_numpy(), w=w)
    assert np.allclose(v1, v2, equal_nan=True)


def test_rolling_sum_vec():
    x = generate_vector()
    w = 5
    v1 = x.rolling(min_periods=1, window=w).sum().to_numpy()
    v2 = _rolling_sum_vec_numba(x.to_numpy(), w=w)
    assert np.allclose(v1, v2, equal_nan=True)


def test_rolling_qv():
    x = generate_vector()
    w = 5
    v1 = x.diff().apply(lambda x: np.power(x, 2)).rolling(min_periods=1, window=w).sum().to_numpy()
    v2 = _rolling_quadratic_variation_vec_numba(x.to_numpy(), w=w)
    assert np.allclose(v1, v2, equal_nan=True)