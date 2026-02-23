import pytest
from src.calculator import add, divide, is_even

# Tests for add function
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),                # positive integers
    (-1, -1, -2),             # negative integers
    (0, 0, 0),                # zeros
    (0, 5, 5),                # zero and positive
    (-5, 5, 0),               # negative and positive
    (2.5, 2.5, 5.0),          # floats
    (1e10, 1e10, 2e10),       # very large numbers
    (-1e10, 1e10, 0),          # large negative and positive
])
def test_add(a, b, expected):
    assert add(a, b) == expected


# Tests for divide function
@pytest.mark.parametrize("a,b,expected", [
    (10, 2, 5),               # positive integers
    (-10, 2, -5),             # negative numerator
    (10, -2, -5),             # negative denominator
    (-10, -2, 5),             # both negative
    (0, 5, 0),               # zero numerator
    (5.0, 2, 2.5),           # float result
    (5, 2.0, 2.5),           # float denominator
])
def test_divide(a, b, expected):
    assert divide(a, b) == expected


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


# Tests for is_even function
@pytest.mark.parametrize("num,expected", [
    (2, True),                # even positive
    (3, False),               # odd positive
    (-2, True),               # even negative
    (-3, False),              # odd negative
    (0, True),                # zero
    (10**10, True),           # very large even
    (10**10 + 1, False),      # very large odd
])
def test_is_even(num, expected):
    assert is_even(num) == expected
