import pytest
from src.calculator import modulo

# Positive Test Cases

def test_modulo_positive_a_greater_than_b():
    assert modulo(10, 3) == 1

def test_modulo_positive_a_less_than_b():
    assert modulo(3, 10) == 3

def test_modulo_a_zero():
    assert modulo(0, 5) == 0

def test_modulo_a_negative_b_positive():
    assert modulo(-10, 3) == 2

def test_modulo_a_positive_b_negative():
    assert modulo(10, -3) == -2

def test_modulo_a_negative_b_negative():
    assert modulo(-10, -3) == -1

# Negative Test Case

def test_modulo_b_zero_raises_valueerror():
    with pytest.raises(ValueError, match="Cannot modulo by zero"):
        modulo(10, 0)
