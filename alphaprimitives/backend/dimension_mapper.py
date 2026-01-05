from __future__ import annotations

from sympy.core.expr import Expr
import inspect
from sympy import S

class DimensionMapper:
    # --- Math: Arithmetic ---
    @staticmethod
    def add(x: Expr, y: Expr) -> Expr:
        return x

    @staticmethod
    def sub(x: Expr, y: Expr) -> Expr:
        return x

    @staticmethod
    def mul(x: Expr, y: Expr) -> Expr:
        return x * y

    @staticmethod
    def div(x: Expr, y: Expr) -> Expr:
        return x / y

    # --- Math: Nonlinear ---
    @staticmethod
    def power(x: Expr, v: float) -> Expr:
        return x ** v

    @staticmethod
    def log1p(x: Expr) -> Expr:
        return S.one

    @staticmethod
    def abs(x: Expr) -> Expr:
        return x

    @staticmethod
    def sigmoid(x: Expr) -> Expr:
        return S.one

    @staticmethod
    def tanh(x: Expr) -> Expr:
        return S.one

    @staticmethod
    def relu(x: Expr) -> Expr:
        return S.one

    # --- Rolling: Moving Averages ---
    @staticmethod
    def sma(x: Expr, w: int) -> Expr:
        return x

    @staticmethod
    def ema(x: Expr, alpha: float) -> Expr:
        return x

    @staticmethod
    def rolling_median(x: Expr, w: int) -> Expr:
        return x

    @staticmethod
    def savgol_smoothing(x: Expr, w: int = 3, polyorder: int = 3) -> Expr:
        return x

    @staticmethod
    def wma(x: Expr, w: int) -> Expr:
        return x

    @staticmethod
    def hull_moving_average(x: Expr, w: int) -> Expr:
        return x

    # --- Rolling: Stats ---
    @staticmethod
    def rolling_var(x: Expr, w: int) -> Expr:
        return x ** 2

    @staticmethod
    def rolling_std(x: Expr, w: int) -> Expr:
        return x

    @staticmethod
    def rolling_skew(x: Expr, w: int) -> Expr:
        return x

    @staticmethod
    def rolling_kurt(x: Expr, w: int) -> Expr:
        return x

    # --- Rolling: Other ---
    @staticmethod
    def rolling_corr(x: Expr, y: Expr, w: int) -> Expr:
        return x

    @staticmethod
    def rolling_cov(x: Expr, y: Expr, w: int) -> Expr:
        return x * y

    @staticmethod
    def rolling_sum(x: Expr, w: int) -> Expr:
        return x

    @staticmethod
    def rolling_prod(x: Expr, w: int) -> Expr:
        return x ** w

    @staticmethod
    def rolling_quadratic_variation(x: Expr, w: int) -> Expr:
        return x ** 2

    # --- Rolling: Sort Based ---
    @staticmethod
    def rolling_max(x: Expr, w: int) -> Expr:
        return x

    @staticmethod
    def rolling_min(x: Expr, w: int) -> Expr:
        return x

    @staticmethod
    def rolling_rank(x: Expr, w: int) -> Expr:
        return S.one

    @staticmethod
    def rolling_argmin(x: Expr, w: int) -> Expr:
        return S.one

    @staticmethod
    def rolling_argmax(x: Expr, w: int) -> Expr:
        return S.one

    @staticmethod
    def rolling_quantile(x: Expr, w: int, percentile: float) -> Expr:
        return x

    @staticmethod
    def rolling_range(x: Expr, w: int) -> Expr:
        return x

    @staticmethod
    def diff(x: Expr, d: int) -> Expr:
        return x

    @staticmethod
    def delay(x: Expr, d: int) -> Expr:
        return x

    @staticmethod
    def greater_than(x: Expr, y: Expr) -> Expr:
        return S.one

    @staticmethod
    def greater_equal(x: Expr, y: Expr) -> Expr:
        return S.one

    @staticmethod
    def lower_than(x: Expr, y: Expr) -> Expr:
        return S.one

    @staticmethod
    def lower_equal(x: Expr, y: Expr) -> Expr:
        return S.one

    @staticmethod
    def equal(x: Expr, y: Expr) -> Expr:
        return S.one

    @staticmethod
    def not_equal(x: Expr, y: Expr) -> Expr:
        return S.one

    @staticmethod
    def demean_cross_sectional(x: Expr) -> Expr:
        return x

    @staticmethod
    def cs_mean(x: Expr) -> Expr:
        return x

    @staticmethod
    def cs_rank(x: Expr) -> Expr:
        return S.one

    @staticmethod
    def cs_percentile(x: Expr) -> Expr:
        return S.one

    @staticmethod
    def cs_zscore(x: Expr) -> Expr:
        return x

    @staticmethod
    def cs_range_normalize(x: Expr) -> Expr:
        return S.one

    @staticmethod
    def cs_divergence(x: Expr) -> Expr:
        return x ** 2

    @staticmethod
    def cs_winsorize(x: Expr, percentile: float = 0.01) -> Expr:
        return x

    @staticmethod
    def cs_resid(x: Expr, y: Expr) -> Expr:
        return x


def apply_dimension_map_from_string(function_name: str, args: dict) -> Expr:
    function = list(filter(
        lambda x: x[0] == function_name,
        inspect.getmembers(DimensionMapper))
    )[0][1]
    return function(**args)