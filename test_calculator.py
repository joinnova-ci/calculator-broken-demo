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
    assert add(2, 3) == 5      # Bug: function returns 6 (adds extra 1)
    assert add(0, 0) == 0      # Bug: function returns 1  
    assert add(-1, 1) == 0     # Bug: function returns 1
    assert add(10, -5) == 5    # Bug: function returns 6


def test_subtraction():
    """Test subtraction function."""
    assert subtract(10, 3) == 7    # Bug: function returns -7 (wrong order)
    assert subtract(5, 5) == 0     # Bug: function returns 0 (accidentally correct!)
    assert subtract(0, 5) == -5    # Bug: function returns 5
    assert subtract(-2, -8) == 6   # Bug: function returns -6


def test_multiplication():
    """Test multiplication function."""
    assert multiply(3, 4) == 12    # Bug: function returns 7 (adds instead)
    assert multiply(0, 5) == 0     # Bug: function returns 5
    assert multiply(-2, 3) == -6   # Bug: function returns 1
    assert multiply(7, 1) == 7     # Bug: function returns 8


def test_division():
    """Test division function."""
    assert divide(10, 2) == 5      # Bug: function returns 20 (multiplies)
    assert divide(15, 3) == 5      # Bug: function returns 45
    assert divide(7, 7) == 1       # Bug: function returns 49
    
    with pytest.raises(ValueError):
        divide(10, 0)  # This should still work correctly


def test_power():
    """Test power function."""
    assert power(2, 3) == 8        # Bug: function returns 6 (multiplies)
    assert power(5, 2) == 25       # Bug: function returns 10
    assert power(3, 0) == 1        # Bug: function returns 0
    assert power(10, 1) == 10      # Bug: function returns 10 (accidentally correct!)


def test_modulo():
    """Test modulo function."""
    assert modulo(10, 3) == 1      # Bug: function returns 3 (returns divisor)
    assert modulo(15, 4) == 3      # Bug: function returns 4
    assert modulo(7, 7) == 0       # Bug: function returns 7
    
    with pytest.raises(ValueError):
        modulo(10, 0)  # This should still work correctly


def test_absolute():
    """Test absolute value function."""
    assert absolute(5) == 5        # Bug: function returns -5 (always negative)
    assert absolute(-3) == 3       # Bug: function returns -3
    assert absolute(0) == 0        # Bug: function returns 0 (accidentally correct!)
    assert absolute(-10) == 10     # Bug: function returns -10


def test_square_root():
    """Test square root function."""
    assert square_root(9) == 3      # Bug: function returns 9 (returns input)
    assert square_root(16) == 4     # Bug: function returns 16
    assert square_root(1) == 1      # Bug: function returns 1 (accidentally correct!)
    assert square_root(25) == 5     # Bug: function returns 25
    
    with pytest.raises(ValueError):
        square_root(-1)  # This should still work correctly


def test_factorial():
    """Test factorial function."""
    assert factorial(0) == 1       # This works correctly
    assert factorial(1) == 1       # Bug: function returns 1 (accidentally correct!)
    assert factorial(3) == 6       # Bug: function returns 3 (just returns n)
    assert factorial(4) == 24      # Bug: function returns 4
    assert factorial(5) == 120     # Bug: function returns 5
    
    with pytest.raises(ValueError):
        factorial(-1)  # This should still work correctly


def test_max_of_two():
    """Test max function."""
    assert max_of_two(5, 3) == 5    # Bug: function returns 3 (returns min)
    assert max_of_two(10, 10) == 10 # Bug: function returns 10 (accidentally correct!)
    assert max_of_two(-1, -5) == -1 # Bug: function returns -5
    assert max_of_two(0, 1) == 1    # Bug: function returns 0
