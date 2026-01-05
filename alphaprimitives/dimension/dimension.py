from copy import deepcopy
from fractions import Fraction
from typing import Dict


class Dimension:
    def __init__(self, unit: Dict[str, Fraction], max_denom: int = 12):
        self._max_denom = max_denom
        self._base_units: Dict[str, Fraction] = self._normalize(unit)

    @classmethod
    def from_name_and_fraction(cls, name: str, power_exponent: Fraction, max_denom: int = 12):
        return cls({name: power_exponent}, max_denom)

    @classmethod
    def from_name_and_float(cls, name: str, power_exponent: float, max_denom: int = 12):
        return cls({name: Fraction(power_exponent).limit_denominator(max_denom)}, max_denom)

    @property
    def base_units(self) -> Dict[str, Fraction]:
        return self._base_units

    def is_dimensionless(self) -> bool:
        return len(self._base_units) == 0

    def _normalize(self, base_units: Dict[str, Fraction]) -> Dict[str, Fraction]:
        cleaned = {k: Fraction(v).limit_denominator(self._max_denom) for k, v in base_units.items() if v != 0}
        return dict(cleaned)

    def __eq__(self, other: 'Dimension') -> bool:
        if not isinstance(other, Dimension):
            return False
        return self._base_units == other._base_units

    def __add__(self, other: 'Dimension') -> 'Dimension':
        if not isinstance(other, Dimension):
            raise TypeError(f"unsupported operand type(s) for +: '{type(self)}' and {type(other)}")
        if self != other:
            raise ValueError(f"cannot add because dimensions don't match")
        return Dimension(dict(self._base_units), self._max_denom)

    def __sub__(self, other: 'Dimension') -> 'Dimension':
        if not isinstance(other, Dimension):
            raise TypeError(f"unsupported operand type(s) for +: '{type(self)}' and {type(other)}")
        if self != other:
            raise ValueError(f"cannot subtract because dimensions don't match")
        return Dimension(dict(self._base_units), self._max_denom)

    def __mul__(self, other: 'Dimension') -> 'Dimension':
        if not isinstance(other, Dimension):
            raise TypeError(f"unsupported operand type(s) for *: '{type(other)}'")
        out: Dict[str, Fraction] = dict(self._base_units)
        for k, v in other._base_units.items():
            out[k] = self._base_units.get(k, Fraction(0)) + v
        return Dimension(self._normalize(out), self._max_denom)

    def __truediv__(self, other: 'Dimension') -> 'Dimension':
        if not isinstance(other, Dimension):
            raise TypeError(f"unsupported operand type(s) for /: '{type(other)}'")
        out: Dict[str, Fraction] = deepcopy(self._base_units)
        for k, v in other._base_units.items():
            out[k] = out.get(k, Fraction(0)) - v
        return Dimension(self._normalize(out), self._max_denom)

    def __pow__(self, power: Fraction | float, modulo=None) -> "Dimension":
        out = {k: v * power for k, v in self._base_units.items()}
        return Dimension(self._normalize(out), self._max_denom)

    def __str__(self) -> str:
        if not self._base_units:
            return "1"
        parts = []
        for k in sorted(self._base_units):  # фиксированный порядок
            p = self._base_units[k]
            if p == 1:
                parts.append(k)
            elif p > 0:
                parts.append(f"{k}^{p}")
            else:
                parts.append(f"{k}^({p})")
        return " * ".join(parts)