# Debugging Exercise: Fix the Buggy Calculator

This is a simple project with a debugging exercise. The calculator module has a bug in the `divide` function that causes tests to fail. Your task is to:

1. Set up the project using UV
2. Run the failing test
3. Use a debugger to identify and fix the bug

## Setup Instructions

First, ensure you have Python 3.8+ and UV installed. If you don't have UV yet, you can install it by following the instructions at [UV's GitHub repository](https://github.com/astral-sh/uv).

```bash
# Clone the repository (if you haven't already)
# cd to the project directory

# Create a virtual environment and install dependencies using UV
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -e .
```

## Running the Tests

To run the tests and see the failing test:

```bash
python -m pytest
```

You should see a test failure in the `test_divide` function.

## Debugging Task

1. Use your favorite debugging tool (such as VS Code debugger, PyCharm debugger, or `pdb`) to set breakpoints in the failing test.
2. Step through the code to understand why the test is failing.
3. Fix the bug in the `divide` function in `buggy_calculator/calculator.py`.
4. Run the tests again to confirm your fix works.

### Debugging with VS Code

1. Open the project in VS Code
2. Set breakpoints in the test file by clicking to the left of the line numbers
3. Go to the Run and Debug tab (Ctrl+Shift+D or Cmd+Shift+D)
4. Click "create a launch.json file" and select "Python"
5. Select "pytest" as the debugging configuration
6. Click the play button to start debugging

### Debugging with pdb

Add this line before the test that's failing:

```python
import pdb; pdb.set_trace()
```

Then run the test:

```bash
python -m pytest -xvs tests/test_calculator.py::test_divide
```

### The Bug

The bug is in the `divide` function when handling negative numbers. Think about what could be wrong with the implementation.

Tip: Compare the implementation to your expectations of how division should work.

## Solution

After fixing the bug, all tests should pass. Remember that the correct division of negative numbers should match the behavior of the Python division operator (`/`).
