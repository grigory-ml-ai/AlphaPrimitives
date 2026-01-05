import random
from fractions import Fraction
from string import ascii_lowercase
from alphaprimitives.dimension.dimension import Dimension
from copy import deepcopy
import pytest

def initialize_random_fraction() -> Fraction:
    sign = random.choice([-1, 1])
    return Fraction(sign * random.randint(1, 20), random.randint(1, 20))

def initialize_random_name(n: int = 10) -> str:
    alphabet = list(ascii_lowercase)
    random.shuffle(alphabet)
    return ''.join(alphabet[:n])

def initialize_random_dimension(n_units: int = 4) -> Dimension:
    unit = dict()
    for _ in range(n_units):
        random_fraction = initialize_random_fraction()
        random_name = initialize_random_name()
        unit[random_name] = random_fraction
    return Dimension(unit)


def test_equality():
    dimension1 = initialize_random_dimension()
    dimension2 = initialize_random_dimension()
    assert dimension1 != dimension2
    assert dimension1 == deepcopy(dimension1)
    assert Dimension({}) == Dimension({})

def test_add():
    dimension1 = initialize_random_dimension()
    dimension2 = initialize_random_dimension()
    with pytest.raises(ValueError):
        dimension2 + (dimension1 * dimension2)
    assert dimension1 + dimension1 == dimension1

def test_sub():
    dimension1 = initialize_random_dimension()
    dimension2 = initialize_random_dimension()
    with pytest.raises(ValueError):
        dimension2 - (dimension1 * dimension2)
    assert dimension1 - dimension1 == dimension1

def test_mul():
    dimension1 = initialize_random_dimension()
    dimension2 = initialize_random_dimension()
    dimension1 * dimension2

def test_div():
    dimension1 = initialize_random_dimension()
    assert dimension1 / deepcopy(dimension1) == Dimension({})
