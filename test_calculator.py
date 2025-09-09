"""
Tests for the broken calculator - these will all fail!
=====================================================

Every test in this file will fail because the calculator functions have bugs.
This is perfect for demonstrating Nova CI-Rescue's ability to:
1. Detect multiple failing tests
2. Analyze what each test expects vs what it gets  
3. Fix all the bugs automatically
4. Verify all tests pass

Run: pytest test_calculator.py -v
Then: nova fix
"""

import pytest
from calculator import (
    add, subtract, multiply, divide, power, modulo,
    absolute, square_root, factorial, max_of_two
)


def test_addition():
    """Test addition function."""
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    assert add(10, -5) == 5


def test_subtraction():
    """Test subtraction function."""
    assert subtract(10, 3) == 7
    assert subtract(5, 5) == 0
    assert subtract(0, 5) == -5
    assert subtract(-2, -8) == 6


def test_multiplication():
    """Test multiplication function."""
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0
    assert multiply(-2, 3) == -6
    assert multiply(7, 1) == 7


def test_division():
    """Test division function."""
    assert divide(10, 2) == 5
    assert divide(15, 3) == 5
    assert divide(7, 7) == 1
    
    with pytest.raises(ValueError):
        divide(10, 0)  # This should still work correctly


def test_power():
    """Test power function."""
    assert power(2, 3) == 8
    assert power(5, 2) == 25
    assert power(3, 0) == 1
    assert power(10, 1) == 10


def test_modulo():
    """Test modulo function."""
    assert modulo(10, 3) == 1
    assert modulo(15, 4) == 3
    assert modulo(7, 7) == 0
    
    with pytest.raises(ValueError):
        modulo(10, 0)  # This should still work correctly


def test_absolute():
    """Test absolute value function."""
    assert absolute(5) == 5
    assert absolute(-3) == 3
    assert absolute(0) == 0
    assert absolute(-10) == 10


def test_square_root():
    """Test square root function."""
    assert square_root(9) == 3
    assert square_root(16) == 4
    assert square_root(1) == 1
    assert square_root(25) == 5
    
    with pytest.raises(ValueError):
        square_root(-1)  # This should still work correctly


def test_factorial():
    """Test factorial function."""
    assert factorial(0) == 1       # This works correctly
    assert factorial(1) == 1
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120
    
    with pytest.raises(ValueError):
        factorial(-1)  # This should still work correctly


def test_max_of_two():
    """Test max function."""
    assert max_of_two(5, 3) == 5
    assert max_of_two(10, 10) == 10
    assert max_of_two(-1, -5) == -1
    assert max_of_two(0, 1) == 1
