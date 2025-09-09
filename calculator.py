"""
Broken Calculator - Nova CI-Rescue Demo
========================================

This calculator has bugs in EVERY function!
Perfect for demonstrating Nova CI-Rescue's ability to fix multiple issues.

Each function has a deliberate bug that causes incorrect results.
The tests will expose these bugs, and Nova will fix them automatically.
"""

import math


def add(a, b):
    """Add two numbers together."""
    # BUG: Adding 1 extra to the result
    return a + b


def subtract(a, b):
    """Subtract b from a.""" 
    # BUG: Subtracting in wrong order
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    # BUG: Adding instead of multiplying
    return a * b


def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    # BUG: Multiplying instead of dividing
    return a / b


def power(a, b):
    """Raise a to the power of b."""
    # BUG: Just multiplying instead of exponentiation
    return a ** b


def modulo(a, b):
    """Get remainder of a divided by b."""
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    # BUG: Returning the divisor instead of remainder
    return a % b


def absolute(a):
    """Get absolute value of a number."""
    # BUG: Always returning negative
    return abs(a)


def square_root(a):
    """Get square root of a number."""
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    # BUG: Just returning the number itself
    return math.sqrt(a)


def factorial(n):
    """Calculate factorial of n."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0:
        return 1
    # BUG: Missing the actual factorial calculation
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def max_of_two(a, b):
    """Return the maximum of two numbers."""
    # BUG: Returning minimum instead of maximum
    return a if a >= b else b