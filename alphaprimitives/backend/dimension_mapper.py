from __future__ import annotations
import inspect
from pint import Quantity, UnitRegistry



class DimensionMapper:
    def __init__(self, ureg: UnitRegistry):
        self._ureg = ureg

    # --- Math: Arithmetic ---
    def add(self, x: Quantity[float], y: Quantity[float]) -> Quantity[float]:
        return x

    def sub(self, x: Quantity[float], y: Quantity[float]) -> Quantity[float]:
        return x

    def mul(self, x: Quantity[float], y: Quantity[float]) -> Quantity[float]:
        return x * y

    def div(self, x: Quantity[float], y: Quantity[float]) -> Quantity[float]:
        return x / y

    # --- Math: Nonlinear ---
    def power(self, x: Quantity[float], v: float) -> Quantity[float]:
        return x ** v

    def log1p(self, x: Quantity[float]) -> Quantity[float]:
        return self._ureg.Quantity(1, 'dimensionless')

    def abs(self, x: Quantity[float]) -> Quantity[float]:
        return x

    def sigmoid(self, x: Quantity[float]) -> Quantity[float]:
        return self._ureg.Quantity(1, 'dimensionless')

    def tanh(self, x: Quantity[float]) -> Quantity[float]:
        return self._ureg.Quantity(1, 'dimensionless')

    def relu(self, x: Quantity[float]) -> Quantity[float]:
        return self._ureg.Quantity(1, 'dimensionless')

    # --- Rolling: Moving Averages ---
    def sma(self, x: Quantity[float], w: int) -> Quantity[float]:
        return x

    def ema(self, x: Quantity[float], alpha: float) -> Quantity[float]:
        return x

    def rolling_median(self, x: Quantity[float], w: int) -> Quantity[float]:
        return x

    def savgol_smoothing(self, x: Quantity[float], w: int = 3, polyorder: int = 3) -> Quantity[float]:
        return x

    def wma(self, x: Quantity[float], w: int) -> Quantity[float]:
        return x

    def hull_moving_average(self, x: Quantity[float], w: int) -> Quantity[float]:
        return x

    # --- Rolling: Stats ---
    def rolling_var(self, x: Quantity[float], w: int) -> Quantity[float]:
        return x ** 2

    def rolling_std(self, x: Quantity[float], w: int) -> Quantity[float]:
        return x

    def rolling_skew(self, x: Quantity[float], w: int) -> Quantity[float]:
        return x

    def rolling_kurt(self, x: Quantity[float], w: int) -> Quantity[float]:
        return x

    # --- Rolling: Other ---
    def rolling_corr(self, x: Quantity[float], y: Quantity[float], w: int) -> Quantity[float]:
        return x

    def rolling_cov(self, x: Quantity[float], y: Quantity[float], w: int) -> Quantity[float]:
        return x * y

    def rolling_sum(self, x: Quantity[float], w: int) -> Quantity[float]:
        return x

    def rolling_prod(self, x: Quantity[float], w: int) -> Quantity[float]:
        return x ** w

    def rolling_quadratic_variation(self, x: Quantity[float], w: int) -> Quantity[float]:
        return x ** 2

    # --- Rolling: Sort Based ---
    def rolling_max(self, x: Quantity[float], w: int) -> Quantity[float]:
        return x

    def rolling_min(self, x: Quantity[float], w: int) -> Quantity[float]:
        return x

    def rolling_rank(self, x: Quantity[float], w: int) -> Quantity[float]:
        return self._ureg.Quantity(1, 'dimensionless')

    def rolling_argmin(self, x: Quantity[float], w: int) -> Quantity[float]:
        return self._ureg.Quantity(1, 'dimensionless')

    def rolling_argmax(self, x: Quantity[float], w: int) -> Quantity[float]:
        return self._ureg.Quantity(1, 'dimensionless')

    def rolling_quantile(self, x: Quantity[float], w: int) -> Quantity[float]:
        return x

    def rolling_range(self, x: Quantity[float], w: int) -> Quantity[float]:
        return x

    def diff(self, x: Quantity[float], d: int) -> Quantity[float]:
        return x

    def delay(self, x: Quantity[float], d: int) -> Quantity[float]:
        return x

    def greater_than(self, x: Quantity[float], y: Quantity[float]) -> Quantity[float]:
        return self._ureg.Quantity(1, 'dimensionless')

    def greater_equal(self, x: Quantity[float], y: Quantity[float]) -> Quantity[float]:
        return self._ureg.Quantity(1, 'dimensionless')

    def lower_than(self, x: Quantity[float], y: Quantity[float]) -> Quantity[float]:
        return self._ureg.Quantity(1, 'dimensionless')

    def lower_equal(self, x: Quantity[float], y: Quantity[float]) -> Quantity[float]:
        return self._ureg.Quantity(1, 'dimensionless')

    def equal(self, x: Quantity[float], y: Quantity[float]) -> Quantity[float]:
        return self._ureg.Quantity(1, 'dimensionless')

    def not_equal(self, x: Quantity[float], y: Quantity[float]) -> Quantity[float]:
        return self._ureg.Quantity(1, 'dimensionless')

    def demean_cross_sectional(self, x: Quantity[float]) -> Quantity[float]:
        return x

    def cs_mean(self, x: Quantity[float]) -> Quantity[float]:
        return x

    def cs_rank(self, x: Quantity[float]) -> Quantity[float]:
        return self._ureg.Quantity(1, 'dimensionless')

    def cs_percentile(self, x: Quantity[float]) -> Quantity[float]:
        return self._ureg.Quantity(1, 'dimensionless')

    def cs_zscore(self, x: Quantity[float]) -> Quantity[float]:
        return x

    def cs_range_normalize(self, x: Quantity[float]) -> Quantity[float]:
        return self._ureg.Quantity(1, 'dimensionless')

    def cs_divergence(self, x: Quantity[float]) -> Quantity[float]:
        return x ** 2

    def cs_winsorize(self, x: Quantity[float], percentile: float = 0.01) -> Quantity[float]:
        return x

    def cs_resid(self, x: Quantity[float], y: Quantity[float]) -> Quantity[float]:
        return x


def apply_dimension_map_from_string(function_name: str, args: dict, ureg: UnitRegistry) -> Quantity[float]:
    dimension_mapper = DimensionMapper(ureg)
    function = list(filter(
        lambda x: x[0] == function_name,
        inspect.getmembers(dimension_mapper))
    )[0][1]
    return function(**args)