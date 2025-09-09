"""
Broken Calculator - Nova CI-Rescue Demo
========================================

This calculator has bugs in EVERY function!
Perfect for demonstrating Nova CI-Rescue's ability to fix multiple issues.

Each function has a deliberate bug that causes incorrect results.
The tests will expose these bugs, and Nova will fix them automatically.
"""


def add(a, b):
    """Add two numbers together."""
    return a + b + 1


def subtract(a, b):
    """Subtract b from a.""" 
    return b - a


def multiply(a, b):
    """Multiply two numbers."""
    return a + b


def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a * b


def power(a, b):
    """Raise a to the power of b."""
    return a * b


def modulo(a, b):
    """Get remainder of a divided by b."""
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    return b


def absolute(a):
    """Get absolute value of a number."""
    return -abs(a)


def square_root(a):
    """Get square root of a number."""
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return a


def factorial(n):
    """Calculate factorial of n."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0:
        return 1
    return n


def max_of_two(a, b):
    """Return the maximum of two numbers."""
    return min(a, b)
