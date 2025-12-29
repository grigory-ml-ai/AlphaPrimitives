import inspect

import pandas as pd

from alphaprimitives.different import difference, logical, cross_sectional
from alphaprimitives.math import arithmetic, nonlinear
from alphaprimitives.rolling import (
    moving_average,
    rolling_corr,
    rolling_cov,
    rolling_sum,
    rolling_stats,
    rolling_cumprod,
    rolling_func_sort_based,
    rolling_quadratic_variation
)


class PanelBackendPandas:
    # --- Math: Arithmetic ---
    def add(self, x: pd.DataFrame, y: pd.DataFrame) -> pd.DataFrame:
        return arithmetic.add(x, y)

    def sub(self, x: pd.DataFrame, y: pd.DataFrame) -> pd.DataFrame:
        return arithmetic.sub(x, y)

    def mul(self, x: pd.DataFrame, y: pd.DataFrame) -> pd.DataFrame:
        return arithmetic.mul(x, y)

    def div(self, x: pd.DataFrame, y: pd.DataFrame) -> pd.DataFrame:
        return arithmetic.div(x, y)

    # --- Math: Nonlinear ---
    def power(self, x: pd.DataFrame, v: float) -> pd.DataFrame:
        return nonlinear.power(x, v)

    def log1p(self, x: pd.DataFrame) -> pd.DataFrame:
        return nonlinear.log1p(x)

    def abs(self, x: pd.DataFrame) -> pd.DataFrame:
        return nonlinear.abs(x)

    def sigmoid(self, x: pd.DataFrame) -> pd.DataFrame:
        return nonlinear.sigmoid(x)

    def tanh(self, x: pd.DataFrame) -> pd.DataFrame:
        return nonlinear.tanh(x)

    def relu(self, x: pd.DataFrame) -> pd.DataFrame:
        return nonlinear.relu(x)

    # --- Rolling: Moving Averages ---
    def sma(self, x: pd.DataFrame, w: int) -> pd.DataFrame:
        return moving_average.sma(x, w)

    def ema(self, x: pd.DataFrame, alpha: float) -> pd.DataFrame:
        return moving_average.ema(x, alpha)

    def rolling_median(self, x: pd.DataFrame, w: int) -> pd.DataFrame:
        return moving_average.rolling_median(x, w)

    def savgol_smoothing(self, x: pd.DataFrame, w: int = 3, polyorder: int = 3) -> pd.DataFrame:
        return moving_average.savgol_smoothing(x, w, polyorder)

    def wma(self, x: pd.DataFrame, w: int) -> pd.DataFrame:
        return moving_average.wma(x, w)

    def hull_moving_average(self, x: pd.DataFrame, w: int) -> pd.DataFrame:
        return moving_average.hull_moving_average(x, w)

    # --- Rolling: Stats ---
    def rolling_var(self, x: pd.DataFrame, w: int) -> pd.DataFrame:
        return rolling_stats.rolling_var(x, w)

    def rolling_std(self, x: pd.DataFrame, w: int) -> pd.DataFrame:
        return rolling_stats.rolling_std(x, w)

    def rolling_skew(self, x: pd.DataFrame, w: int) -> pd.DataFrame:
        return rolling_stats.rolling_skew(x, w)

    def rolling_kurt(self, x: pd.DataFrame, w: int) -> pd.DataFrame:
        return rolling_stats.rolling_kurt(x, w)

    # --- Rolling: Other ---
    def rolling_corr(self, x: pd.DataFrame, y: pd.DataFrame, w: int) -> pd.DataFrame:
        return rolling_corr.rolling_corr(x, y, w)

    def rolling_cov(self, x: pd.DataFrame, w: int) -> pd.DataFrame:
        return rolling_cov.rolling_cov(x, w)

    def rolling_sum(self, x: pd.DataFrame, w: int) -> pd.DataFrame:
        return rolling_sum.rolling_sum(x, w)

    def rolling_prod(self, x: pd.DataFrame, w: int) -> pd.DataFrame:
        return rolling_cumprod.rolling_prod(x, w)

    def rolling_quadratic_variation(self, x: pd.DataFrame, w: int) -> pd.DataFrame:
        return rolling_quadratic_variation.rolling_quadratic_variation(x, w)

    # --- Rolling: Sort Based ---
    def rolling_max(self, x: pd.DataFrame, w: int) -> pd.DataFrame:
        return rolling_func_sort_based.rolling_max(x, w)

    def rolling_min(self, x: pd.DataFrame, w: int) -> pd.DataFrame:
        return rolling_func_sort_based.rolling_min(x, w)

    def rolling_rank(self, x: pd.DataFrame, w: int) -> pd.DataFrame:
        return rolling_func_sort_based.rolling_rank(x, w)

    def rolling_argmin(self, x: pd.DataFrame, w: int) -> pd.DataFrame:
        return rolling_func_sort_based.rolling_argmin(x, w)

    def rolling_argmax(self, x: pd.DataFrame, w: int) -> pd.DataFrame:
        return rolling_func_sort_based.rolling_argmax(x, w)

    def rolling_quantile(self, x: pd.DataFrame, w: int) -> pd.DataFrame:
        return rolling_func_sort_based.rolling_quantile(x, w)

    def rolling_deviance(self, x: pd.DataFrame, w: int) -> pd.DataFrame:
        return rolling_func_sort_based.rolling_deviance(x, w)

    def diff(self, x: pd.DataFrame, d: int) -> pd.DataFrame:
        return difference.diff(x, d)

    def delay(self, x: pd.DataFrame, d: int) -> pd.DataFrame:
        return difference.delay(x, d)

    def greater_than(self, x: pd.DataFrame, y: pd.DataFrame) -> pd.DataFrame:
        return logical.greater_than(x, y)

    def greater_equal(self, x: pd.DataFrame, y: pd.DataFrame) -> pd.DataFrame:
        return logical.greater_equal(x, y)

    def lower_than(self, x: pd.DataFrame, y: pd.DataFrame) -> pd.DataFrame:
        return logical.lower_than(x, y)

    def lower_equal(self, x: pd.DataFrame, y: pd.DataFrame) -> pd.DataFrame:
        return logical.lower_equal(x, y)

    def equal(self, x: pd.DataFrame, y: pd.DataFrame) -> pd.DataFrame:
        return logical.equal(x, y)

    def not_equal(self, x: pd.DataFrame, y: pd.DataFrame) -> pd.DataFrame:
        return logical.not_equal(x, y)

    def demean_cross_sectional(self, x: pd.DataFrame) -> pd.DataFrame:
        return cross_sectional.demean_cross_sectional(x)

    def cs_mean(self, x: pd.DataFrame) -> pd.DataFrame:
        return cross_sectional.cs_mean(x)

    def cs_rank(self, x: pd.DataFrame) -> pd.DataFrame:
        return cross_sectional.cs_rank(x)

    def cs_percentile(self, x: pd.DataFrame) -> pd.DataFrame:
        return cross_sectional.cs_percentile(x)

    def cs_zscore(self, x: pd.DataFrame) -> pd.DataFrame:
        return cross_sectional.cs_zscore(x)

    def cs_range_normalize(self, x: pd.DataFrame) -> pd.DataFrame:
        return cross_sectional.cs_range_normalize(x)

    def cs_divergence(self, x: pd.DataFrame) -> pd.DataFrame:
        return cross_sectional.cs_divergence(x)

    def cs_winsorize(self, x: pd.DataFrame, percentile: float = 0.01) -> pd.DataFrame:
        return cross_sectional.cs_winsorize(x, percentile)

    def cs_resid(self, x: pd.DataFrame, y: pd.DataFrame) -> pd.DataFrame:
        return cross_sectional.cs_resid(x, y)


def apply_from_string(function_name: str, args: dict):
    backend = PanelBackendPandas()
    function = list(filter(lambda x: x[0] == function_name, inspect.getmembers(backend)))[0][1]
    return function(**args)
