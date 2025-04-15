"""
Main module that demonstrates the calculator functionality.
"""
from buggy_calculator.calculator import add, subtract, multiply, divide


def main():
    """Demonstrate calculator functionality."""
    print("Buggy Calculator Demo")
    print("---------------------")
    
    print(f"Addition: 5 + 3 = {add(5, 3)}")
    print(f"Subtraction: 10 - 4 = {subtract(10, 4)}")
    print(f"Multiplication: 6 * 7 = {multiply(6, 7)}")
    
    try:
        print(f"Division: 8 / 2 = {divide(8, 2)}")
        print(f"Division with negative: -9 / 3 = {divide(-9, 3)}")  # This will show the bug
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main() 