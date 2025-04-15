"""
Test suite for the buggy calculator module.
"""
import pytest
from buggy_calculator.calculator import add, subtract, multiply, divide


def test_add():
    """Test the add function."""
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    """Test the subtract function."""
    assert subtract(3, 2) == 1
    assert subtract(1, 1) == 0
    assert subtract(0, 5) == -5


def test_multiply():
    """Test the multiply function."""
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0


def test_divide():
    """Test the divide function with a variety of inputs."""
    assert divide(6, 3) == 2
    assert divide(0, 5) == 0
    
    # These tests will fail due to the bug in the division function
    assert divide(-6, 3) == -2  # This will fail
    assert divide(-7, 2) == -3.5  # This will fail
    
    with pytest.raises(ValueError):
        divide(5, 0)  # Should raise ValueError 