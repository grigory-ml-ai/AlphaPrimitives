from __future__ import annotations
from fractions import Fraction
from alphaprimitives.dimension.dimension import Dimension
import inspect
from sympy import S
from beartype import beartype

@beartype
class DimensionMapper:
    # --- Math: Arithmetic ---
    @staticmethod
    def add(x: Dimension, y: Dimension) -> Dimension:
        if x != y:
            raise ValueError(f"Cannot add two dimensions: {x} and {y}")
        return x + y

    @staticmethod
    def sub(x: Dimension, y: Dimension) -> Dimension:
        if x != y:
            raise ValueError(f"Cannot subtract two dimensions: {x} and {y}")
        return x - y

    @staticmethod
    def mul(x: Dimension, y: Dimension) -> Dimension:
        return x * y


    @staticmethod
    def div(x: Dimension, y: Dimension) -> Dimension:
        return x / y

    # --- Math: Nonlinear ---
    @staticmethod
    def power(x: Dimension, v: float | Fraction) -> Dimension:
        return x ** v

    @staticmethod
    def log1p(x: Dimension) -> Dimension:
        return Dimension({})

    @staticmethod
    def abs(x: Dimension) -> Dimension:
        return x

    @staticmethod
    def sigmoid(x: Dimension) -> Dimension:
        return Dimension({})

    @staticmethod
    def tanh(x: Dimension) -> Dimension:
        return Dimension({})

    @staticmethod
    def relu(x: Dimension) -> Dimension:
        return Dimension({})

    # --- Rolling: Moving Averages ---
    @staticmethod
    def sma(x: Dimension, w: int) -> Dimension:
        return x

    @staticmethod
    def ema(x: Dimension, alpha: float) -> Dimension:
        return x

    @staticmethod
    def rolling_median(x: Dimension, w: int) -> Dimension:
        return x

    @staticmethod
    def savgol_smoothing(x: Dimension, w: int = 3, polyorder: int = 3) -> Dimension:
        return x

    @staticmethod
    def wma(x: Dimension, w: int) -> Dimension:
        return x

    @staticmethod
    def hull_moving_average(x: Dimension, w: int) -> Dimension:
        return x

    # --- Rolling: Stats ---
    @staticmethod
    def rolling_var(x: Dimension, w: int) -> Dimension:
        return x ** 2

    @staticmethod
    def rolling_std(x: Dimension, w: int) -> Dimension:
        return x

    @staticmethod
    def rolling_skew(x: Dimension, w: int) -> Dimension:
        return x

    @staticmethod
    def rolling_kurt(x: Dimension, w: int) -> Dimension:
        return x

    # --- Rolling: Other ---
    @staticmethod
    def rolling_corr(x: Dimension, y: Dimension, w: int) -> Dimension:
        return x

    @staticmethod
    def rolling_cov(x: Dimension, y: Dimension, w: int) -> Dimension:
        return x * y

    @staticmethod
    def rolling_sum(x: Dimension, w: int) -> Dimension:
        return x

    @staticmethod
    def rolling_prod(x: Dimension, w: int) -> Dimension:
        return x ** w

    @staticmethod
    def rolling_quadratic_variation(x: Dimension, w: int) -> Dimension:
        return x ** 2

    # --- Rolling: Sort Based ---
    @staticmethod
    def rolling_max(x: Dimension, w: int) -> Dimension:
        return x

    @staticmethod
    def rolling_min(x: Dimension, w: int) -> Dimension:
        return x

    @staticmethod
    def rolling_rank(x: Dimension, w: int) -> Dimension:
        return Dimension({})

    @staticmethod
    def rolling_argmin(x: Dimension, w: int) -> Dimension:
        return Dimension({})

    @staticmethod
    def rolling_argmax(x: Dimension, w: int) -> Dimension:
        return Dimension({})

    @staticmethod
    def rolling_quantile(x: Dimension, w: int, percentile: float) -> Dimension:
        return x

    @staticmethod
    def rolling_range(x: Dimension, w: int) -> Dimension:
        return x

    @staticmethod
    def diff(x: Dimension, d: int) -> Dimension:
        return x

    @staticmethod
    def delay(x: Dimension, d: int) -> Dimension:
        return x

    @staticmethod
    def greater_than(x: Dimension, y: Dimension) -> Dimension:
        if x != y:
            raise ValueError(f"Cannot compare two dimensions: {x} and {y}")
        return Dimension({})

    @staticmethod
    def greater_equal(x: Dimension, y: Dimension) -> Dimension:
        if x != y:
            raise ValueError(f"Cannot compare two dimensions: {x} and {y}")
        return Dimension({})

    @staticmethod
    def lower_than(x: Dimension, y: Dimension) -> Dimension:
        if x != y:
            raise ValueError(f"Cannot compare two dimensions: {x} and {y}")
        return Dimension({})

    @staticmethod
    def lower_equal(x: Dimension, y: Dimension) -> Dimension:
        if x != y:
            raise ValueError(f"Cannot compare two dimensions: {x} and {y}")
        return Dimension({})

    @staticmethod
    def equal(x: Dimension, y: Dimension) -> Dimension:
        if x != y:
            raise ValueError(f"Cannot compare two dimensions: {x} and {y}")
        return Dimension({})

    @staticmethod
    def not_equal(x: Dimension, y: Dimension) -> Dimension:
        if x != y:
            raise ValueError(f"Cannot compare two dimensions: {x} and {y}")
        return Dimension({})

    @staticmethod
    def demean_cross_sectional(x: Dimension) -> Dimension:
        return x

    @staticmethod
    def cs_mean(x: Dimension) -> Dimension:
        return x

    @staticmethod
    def cs_rank(x: Dimension) -> Dimension:
        return Dimension({})

    @staticmethod
    def cs_percentile(x: Dimension) -> Dimension:
        return Dimension({})

    @staticmethod
    def cs_zscore(x: Dimension) -> Dimension:
        return x

    @staticmethod
    def cs_range_normalize(x: Dimension) -> Dimension:
        return Dimension({})

    @staticmethod
    def cs_divergence(x: Dimension) -> Dimension:
        return x ** 2

    @staticmethod
    def cs_winsorize(x: Dimension, percentile: float = 0.01) -> Dimension:
        return x

    @staticmethod
    def cs_resid(x: Dimension, y: Dimension) -> Dimension:
        return x


def apply_dim_map_from_string(function_name: str, args: dict) -> Dimension:
    function = getattr(DimensionMapper, function_name, None)
    if function is None:
        raise AttributeError(f"Метод {function_name} не найден в DimensionMapper")
    return function(**args)
