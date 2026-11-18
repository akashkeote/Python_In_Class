"""Recursion and Python modules - study notes."""


# ============================================================
# 1. Recursion
# ============================================================
# Recursion means a function calling itself.
# Every recursive function needs:
#   1. Base case: stops the recursion.
#   2. Recursive case: calls the function with a smaller problem.


def factorial(number):
    """Return the factorial of a non-negative integer."""
    if number < 0:
        raise ValueError("factorial is not defined for negative numbers")
    if number == 0:
        return 1
    return number * factorial(number - 1)


print("Factorial of 7:", factorial(7))


def fibonacci(number):
    """Return the number at position `number` in the Fibonacci sequence."""
    if number < 0:
        raise ValueError("position cannot be negative")
    if number == 0 or number == 1:
        return 1
    return fibonacci(number - 1) + fibonacci(number - 2)


print("Fibonacci at position 7:", fibonacci(7))
print("Fibonacci at position 5:", fibonacci(5))


# ============================================================
# 2. Importing the math module
# ============================================================
import math

print("Module type:", type(math))
print("Value of pi:", math.pi)
print("sin(pi / 4):", math.sin(math.pi / 4))

# An alias gives another name to the imported module.
foo = math
print("pi through alias:", foo.pi)

import math as mymath

print("pi through mymath:", mymath.pi)

# Import selected functions when the module name is not needed repeatedly.
from math import cos, sin, tan

print("sin(3.14 / 2):", sin(3.14 / 2))
print("cos(0):", cos(0))
print("tan(0):", tan(0))

# Remove a name with del. The module itself is not deleted from Python.
del foo
del mymath


# ============================================================
# 3. Other useful standard-library modules
# ============================================================
import json
import statistics

print("Mean:", statistics.mean([1, 2, 3]))

# json.loads() converts a JSON string into a Python object.
json_text = '{"name": "akash"}'
print("JSON string to dictionary:", json.loads(json_text))


# ============================================================
# 4. A custom square-root function
# ============================================================
def square_root(number):
    """Return the square root of a non-negative number."""
    if number < 0:
        raise ValueError("square root is not defined for negative numbers")
    return number ** 0.5


print("Square root of 5:", square_root(5))


# ============================================================
# 5. The sys module
# ============================================================
import sys

print("Python version:", sys.version)
print("Module type:", type(sys))
print("Recursion limit:", sys.getrecursionlimit())
print("First path entry:", sys.path[0])

# Add a folder to Python's module search path when required.
# sys.path.append(r"C:\\Users\\akash.keote\\Desktop\\Notes\\17Nov")


# ============================================================
# 6. __pycache__
# ============================================================
# Python may create a __pycache__ folder containing compiled bytecode files
# (.pyc) when a module is imported. These files are generated automatically
# and can be recreated, so deleting them does not delete the source code.
