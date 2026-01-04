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
    @staticmethod
    def add(x: pd.DataFrame, y: pd.DataFrame) -> pd.DataFrame:
        return arithmetic.add(x, y)

    @staticmethod
    def sub(x: pd.DataFrame, y: pd.DataFrame) -> pd.DataFrame:
        return arithmetic.sub(x, y)

    @staticmethod
    def mul(x: pd.DataFrame, y: pd.DataFrame) -> pd.DataFrame:
        return arithmetic.mul(x, y)

    @staticmethod
    def div(x: pd.DataFrame, y: pd.DataFrame) -> pd.DataFrame:
        return arithmetic.div(x, y)

    # --- Math: Nonlinear ---
    @staticmethod
    def power(x: pd.DataFrame, v: float) -> pd.DataFrame:
        return nonlinear.power(x, v)

    @staticmethod
    def log1p(x: pd.DataFrame) -> pd.DataFrame:
        return nonlinear.log1p(x)

    @staticmethod
    def abs(x: pd.DataFrame) -> pd.DataFrame:
        return nonlinear.abs(x)

    @staticmethod
    def sigmoid(x: pd.DataFrame) -> pd.DataFrame:
        return nonlinear.sigmoid(x)

    @staticmethod
    def tanh(x: pd.DataFrame) -> pd.DataFrame:
        return nonlinear.tanh(x)

    @staticmethod
    def relu(x: pd.DataFrame) -> pd.DataFrame:
        return nonlinear.relu(x)

    # --- Rolling: Moving Averages ---
    @staticmethod
    def sma(x: pd.DataFrame, w: int) -> pd.DataFrame:
        return moving_average.sma(x, w)

    @staticmethod
    def ema(x: pd.DataFrame, alpha: float) -> pd.DataFrame:
        return moving_average.ema(x, alpha)

    @staticmethod
    def rolling_median(x: pd.DataFrame, w: int) -> pd.DataFrame:
        return moving_average.rolling_median(x, w)

    @staticmethod
    def savgol_smoothing(x: pd.DataFrame, w: int = 3, polyorder: int = 3) -> pd.DataFrame:
        return moving_average.savgol_smoothing(x, w, polyorder)

    @staticmethod
    def wma(x: pd.DataFrame, w: int) -> pd.DataFrame:
        return moving_average.wma(x, w)

    @staticmethod
    def hull_moving_average(x: pd.DataFrame, w: int) -> pd.DataFrame:
        return moving_average.hull_moving_average(x, w)

    # --- Rolling: Stats ---
    @staticmethod
    def rolling_var(x: pd.DataFrame, w: int) -> pd.DataFrame:
        return rolling_stats.rolling_var(x, w)

    @staticmethod
    def rolling_std(x: pd.DataFrame, w: int) -> pd.DataFrame:
        return rolling_stats.rolling_std(x, w)

    @staticmethod
    def rolling_skew(x: pd.DataFrame, w: int) -> pd.DataFrame:
        return rolling_stats.rolling_skew(x, w)

    @staticmethod
    def rolling_kurt(x: pd.DataFrame, w: int) -> pd.DataFrame:
        return rolling_stats.rolling_kurt(x, w)

    # --- Rolling: Other ---
    @staticmethod
    def rolling_corr(x: pd.DataFrame, y: pd.DataFrame, w: int) -> pd.DataFrame:
        return rolling_corr.rolling_corr(x, y, w)

    @staticmethod
    def rolling_cov(x: pd.DataFrame, w: int) -> pd.DataFrame:
        return rolling_cov.rolling_cov(x, w)

    @staticmethod
    def rolling_sum(x: pd.DataFrame, w: int) -> pd.DataFrame:
        return rolling_sum.rolling_sum(x, w)

    @staticmethod
    def rolling_prod(x: pd.DataFrame, w: int) -> pd.DataFrame:
        return rolling_cumprod.rolling_prod(x, w)

    @staticmethod
    def rolling_quadratic_variation(x: pd.DataFrame, w: int) -> pd.DataFrame:
        return rolling_quadratic_variation.rolling_quadratic_variation(x, w)

    # --- Rolling: Sort Based ---
    @staticmethod
    def rolling_max(x: pd.DataFrame, w: int) -> pd.DataFrame:
        return rolling_func_sort_based.rolling_max(x, w)

    @staticmethod
    def rolling_min(x: pd.DataFrame, w: int) -> pd.DataFrame:
        return rolling_func_sort_based.rolling_min(x, w)

    @staticmethod
    def rolling_rank(x: pd.DataFrame, w: int) -> pd.DataFrame:
        return rolling_func_sort_based.rolling_rank(x, w)

    @staticmethod
    def rolling_argmin(x: pd.DataFrame, w: int) -> pd.DataFrame:
        return rolling_func_sort_based.rolling_argmin(x, w)

    @staticmethod
    def rolling_argmax(x: pd.DataFrame, w: int) -> pd.DataFrame:
        return rolling_func_sort_based.rolling_argmax(x, w)

    @staticmethod
    def rolling_quantile(x: pd.DataFrame, w: int, percentile: float) -> pd.DataFrame:
        return rolling_func_sort_based.rolling_quantile(x, w, percentile)

    @staticmethod
    def rolling_range(x: pd.DataFrame, w: int) -> pd.DataFrame:
        return rolling_func_sort_based.rolling_range(x, w)

    @staticmethod
    def diff(x: pd.DataFrame, d: int) -> pd.DataFrame:
        return difference.diff(x, d)

    @staticmethod
    def delay(x: pd.DataFrame, d: int) -> pd.DataFrame:
        return difference.delay(x, d)

    @staticmethod
    def greater_than(x: pd.DataFrame, y: pd.DataFrame) -> pd.DataFrame:
        return logical.greater_than(x, y)

    @staticmethod
    def greater_equal(x: pd.DataFrame, y: pd.DataFrame) -> pd.DataFrame:
        return logical.greater_equal(x, y)

    @staticmethod
    def lower_than(x: pd.DataFrame, y: pd.DataFrame) -> pd.DataFrame:
        return logical.lower_than(x, y)

    @staticmethod
    def lower_equal(x: pd.DataFrame, y: pd.DataFrame) -> pd.DataFrame:
        return logical.lower_equal(x, y)

    @staticmethod
    def equal(x: pd.DataFrame, y: pd.DataFrame) -> pd.DataFrame:
        return logical.equal(x, y)

    @staticmethod
    def not_equal(x: pd.DataFrame, y: pd.DataFrame) -> pd.DataFrame:
        return logical.not_equal(x, y)

    @staticmethod
    def demean_cross_sectional(x: pd.DataFrame) -> pd.DataFrame:
        return cross_sectional.demean_cross_sectional(x)

    @staticmethod
    def cs_mean(x: pd.DataFrame) -> pd.DataFrame:
        return cross_sectional.cs_mean(x)

    @staticmethod
    def cs_rank(x: pd.DataFrame) -> pd.DataFrame:
        return cross_sectional.cs_rank(x)

    @staticmethod
    def cs_percentile(x: pd.DataFrame) -> pd.DataFrame:
        return cross_sectional.cs_percentile(x)

    @staticmethod
    def cs_zscore(x: pd.DataFrame) -> pd.DataFrame:
        return cross_sectional.cs_zscore(x)

    @staticmethod
    def cs_range_normalize(x: pd.DataFrame) -> pd.DataFrame:
        return cross_sectional.cs_range_normalize(x)

    @staticmethod
    def cs_divergence(x: pd.DataFrame) -> pd.DataFrame:
        return cross_sectional.cs_divergence(x)

    @staticmethod
    def cs_winsorize(x: pd.DataFrame, percentile: float = 0.01) -> pd.DataFrame:
        return cross_sectional.cs_winsorize(x, percentile)

    @staticmethod
    def cs_resid(x: pd.DataFrame, y: pd.DataFrame) -> pd.DataFrame:
        return cross_sectional.cs_resid(x, y)


def apply_from_string(function_name: str, args: dict):
    function = list(filter(lambda x: x[0] == function_name, inspect.getmembers(PanelBackendPandas)))[0][1]
    return function(**args)




