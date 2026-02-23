import pytest
from src.calculator import power


def test_power_positive_integers():
    assert power(2, 3) == 8


def test_power_zero_exponent():
    assert power(5, 0) == 1


def test_power_negative_exponent():
    assert power(2, -2) == 0.25


def test_power_zero_base_positive_exponent():
    assert power(0, 3) == 0


def test_power_zero_base_zero_exponent():
    assert power(0, 0) == 1


def test_power_float_base():
    assert power(2.5, 2) == 6.25


def test_power_negative_base_positive_odd_exponent():
    assert power(-2, 3) == -8


def test_power_negative_base_even_exponent():
    assert power(-2, 4) == 16


def test_power_large_exponent():
    # Just test that it executes and returns the correct result for a large exponent
    large_exp = 100
    base = 1.0001
    expected = base ** large_exp
    assert power(base, large_exp) == expected


def test_power_large_negative_exponent():
    # Very small value due to large negative exponent
    base = 2
    neg_large_exp = -100
    expected = base ** neg_large_exp
    assert power(base, neg_large_exp) == expected


def test_power_fractional_exponent():
    base = 9
    exponent = 0.5
    expected = base ** exponent
    assert power(base, exponent) == expected


# No explicit test for invalid types as function does not handle errors
