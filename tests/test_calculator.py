import pytest
from src.calculator import add, divide, is_even, multiply

# Test add function
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, -1, -2),
    (2.5, 3.5, 6.0),
    (0, 5, 5),
    (-3, 3, 0)
])
def test_add(a, b, expected):
    assert add(a, b) == expected

# Test divide function
@pytest.mark.parametrize("a,b,expected", [
    (6, 3, 2.0),
    (0, 1, 0.0),
    (-6, 3, -2.0),
    (7, 2, 3.5)
])
def test_divide(a, b, expected):
    assert divide(a, b) == expected


def test_divide_zero_division():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)

# Test is_even function
@pytest.mark.parametrize("num,expected", [
    (4, True),
    (3, False),
    (0, True),
    (-2, True),
    (-3, False)
])
def test_is_even(num, expected):
    assert is_even(num) == expected

# Test multiply function
@pytest.mark.parametrize("a,b,expected", [
    (3, 5, 15),
    (0, 10, 0),
    (-2, 3, -6),
    (2.5, 4, 10.0),
    (0, 0, 0)
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected
