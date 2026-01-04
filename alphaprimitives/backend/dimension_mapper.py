from __future__ import annotations

import inspect

from pint import UnitRegistry
from pint.facets.plain import PlainQuantity


class DimensionMapper:
    def __init__(self, ureg: UnitRegistry):
        self._ureg = ureg

    # --- Math: Arithmetic ---
    def add(self, x: PlainQuantity, y: PlainQuantity) -> PlainQuantity:
        return x

    def sub(self, x: PlainQuantity, y: PlainQuantity) -> PlainQuantity:
        return x

    def mul(self, x: PlainQuantity, y: PlainQuantity) -> PlainQuantity:
        return x * y

    def div(self, x: PlainQuantity, y: PlainQuantity) -> PlainQuantity:
        return x / y

    # --- Math: Nonlinear ---
    def power(self, x: PlainQuantity, v: float) -> PlainQuantity:
        return x ** v

    def log1p(self, x: PlainQuantity) -> PlainQuantity:
        return self._ureg.Quantity(1, 'dimensionless')

    def abs(self, x: PlainQuantity) -> PlainQuantity:
        return x

    def sigmoid(self, x: PlainQuantity) -> PlainQuantity:
        return self._ureg.Quantity(1, 'dimensionless')

    def tanh(self, x: PlainQuantity) -> PlainQuantity:
        return self._ureg.Quantity(1, 'dimensionless')

    def relu(self, x: PlainQuantity) -> PlainQuantity:
        return self._ureg.Quantity(1, 'dimensionless')

    # --- Rolling: Moving Averages ---
    def sma(self, x: PlainQuantity, w: int) -> PlainQuantity:
        return x

    def ema(self, x: PlainQuantity, alpha: float) -> PlainQuantity:
        return x

    def rolling_median(self, x: PlainQuantity, w: int) -> PlainQuantity:
        return x

    def savgol_smoothing(self, x: PlainQuantity, w: int = 3, polyorder: int = 3) -> PlainQuantity:
        return x

    def wma(self, x: PlainQuantity, w: int) -> PlainQuantity:
        return x

    def hull_moving_average(self, x: PlainQuantity, w: int) -> PlainQuantity:
        return x

    # --- Rolling: Stats ---
    def rolling_var(self, x: PlainQuantity, w: int) -> PlainQuantity:
        return x ** 2

    def rolling_std(self, x: PlainQuantity, w: int) -> PlainQuantity:
        return x

    def rolling_skew(self, x: PlainQuantity, w: int) -> PlainQuantity:
        return x

    def rolling_kurt(self, x: PlainQuantity, w: int) -> PlainQuantity:
        return x

    # --- Rolling: Other ---
    def rolling_corr(self, x: PlainQuantity, y: PlainQuantity, w: int) -> PlainQuantity:
        return x

    def rolling_cov(self, x: PlainQuantity, y: PlainQuantity, w: int) -> PlainQuantity:
        return x * y

    def rolling_sum(self, x: PlainQuantity, w: int) -> PlainQuantity:
        return x

    def rolling_prod(self, x: PlainQuantity, w: int) -> PlainQuantity:
        return x ** w

    def rolling_quadratic_variation(self, x: PlainQuantity, w: int) -> PlainQuantity:
        return x ** 2

    # --- Rolling: Sort Based ---
    def rolling_max(self, x: PlainQuantity, w: int) -> PlainQuantity:
        return x

    def rolling_min(self, x: PlainQuantity, w: int) -> PlainQuantity:
        return x

    def rolling_rank(self, x: PlainQuantity, w: int) -> PlainQuantity:
        return self._ureg.Quantity(1, 'dimensionless')

    def rolling_argmin(self, x: PlainQuantity, w: int) -> PlainQuantity:
        return self._ureg.Quantity(1, 'dimensionless')

    def rolling_argmax(self, x: PlainQuantity, w: int) -> PlainQuantity:
        return self._ureg.Quantity(1, 'dimensionless')

    def rolling_quantile(self, x: PlainQuantity, w: int, percentile: float) -> PlainQuantity:
        return x

    def rolling_range(self, x: PlainQuantity, w: int) -> PlainQuantity:
        return x

    def diff(self, x: PlainQuantity, d: int) -> PlainQuantity:
        return x

    def delay(self, x: PlainQuantity, d: int) -> PlainQuantity:
        return x

    def greater_than(self, x: PlainQuantity, y: PlainQuantity) -> PlainQuantity:
        return self._ureg.Quantity(1, 'dimensionless')

    def greater_equal(self, x: PlainQuantity, y: PlainQuantity) -> PlainQuantity:
        return self._ureg.Quantity(1, 'dimensionless')

    def lower_than(self, x: PlainQuantity, y: PlainQuantity) -> PlainQuantity:
        return self._ureg.Quantity(1, 'dimensionless')

    def lower_equal(self, x: PlainQuantity, y: PlainQuantity) -> PlainQuantity:
        return self._ureg.Quantity(1, 'dimensionless')

    def equal(self, x: PlainQuantity, y: PlainQuantity) -> PlainQuantity:
        return self._ureg.Quantity(1, 'dimensionless')

    def not_equal(self, x: PlainQuantity, y: PlainQuantity) -> PlainQuantity:
        return self._ureg.Quantity(1, 'dimensionless')

    def demean_cross_sectional(self, x: PlainQuantity) -> PlainQuantity:
        return x

    def cs_mean(self, x: PlainQuantity) -> PlainQuantity:
        return x

    def cs_rank(self, x: PlainQuantity) -> PlainQuantity:
        return self._ureg.Quantity(1, 'dimensionless')

    def cs_percentile(self, x: PlainQuantity) -> PlainQuantity:
        return self._ureg.Quantity(1, 'dimensionless')

    def cs_zscore(self, x: PlainQuantity) -> PlainQuantity:
        return x

    def cs_range_normalize(self, x: PlainQuantity) -> PlainQuantity:
        return self._ureg.Quantity(1, 'dimensionless')

    def cs_divergence(self, x: PlainQuantity) -> PlainQuantity:
        return x ** 2

    def cs_winsorize(self, x: PlainQuantity, percentile: float = 0.01) -> PlainQuantity:
        return x

    def cs_resid(self, x: PlainQuantity, y: PlainQuantity) -> PlainQuantity:
        return x


def apply_dimension_map_from_string(function_name: str, args: dict, ureg: UnitRegistry) -> PlainQuantity:
    dimension_mapper = DimensionMapper(ureg)
    function = list(filter(
        lambda x: x[0] == function_name,
        inspect.getmembers(dimension_mapper))
    )[0][1]
    return function(**args)