def add(a, b):
    """Adds two numbers."""
    return a + b

def divide(a, b):
    """Divides a by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def is_even(num):
    """Returns True if num is even, else False."""
    return num % 2 == 0


def power(base, exponent):
    """Calculates base raised to the power of exponent."""
    return base ** exponent

