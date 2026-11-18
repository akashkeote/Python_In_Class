"""Exception handling - study notes."""
from typing import ValuesView


# ============================================================
# 1. What is exception handling?
# ============================================================
# An exception is an error that occurs while a program is running.
# try     : code that may produce an error
# except  : handles the error
# else    : runs only when no error occurs
# finally : always runs


# ============================================================
# 2. Base Exception class and raise
# ============================================================
def add_numbers(first_number, second_number):
    """Add two numbers only when both are between 0 and 100."""
    if first_number < 0 or second_number < 0:
        raise Exception("numbers cannot be negative")
    if first_number > 100 or second_number > 100:
        raise Exception("numbers cannot be greater than 100")
    return first_number + second_number


try:
    print("Addition result:", add_numbers(5, 6))
    print("Addition result:", add_numbers(-5, 6))
except Exception as error:
    print("Exception handled:", error)


# ============================================================
# 3. ZeroDivisionError
# ============================================================
def divide(first_number, second_number):
    """Divide two numbers and handle division by zero."""
    try:
        result = first_number / second_number
    except ZeroDivisionError:
        print("Error: a number cannot be divided by zero")
    else:
        print("Division result:", result)
    finally:
        print("Division operation finished")


divide(10, 2)
divide(10, 0)


# ============================================================
# 4. ValueError
# ============================================================
# ValueError is raised when a value has an invalid format or type
# for the requested operation, such as int("hello").
def convert_to_integer(value):
    """Convert a value to int and handle invalid text."""
    try:
        return int(value)
    except ValueError:
        print("Error: value must contain a valid integer")
        return None


print("Converted value:", convert_to_integer("25"))
print("Converted value:", convert_to_integer("twenty-five"))


# ============================================================
# 5. Important rule
# ============================================================
# `except` must directly follow its `try` block. When there are multiple
# handlers, catch specific exceptions first and general Exception last.
def process_value(value):
    """Show the correct order of specific and general exception handlers."""
    try:
        if value == "zero":
            return 10 / 0
        number = int(value)
        if number < 0:
            raise Exception("number cannot be negative")
        return number
    except ValueError:
        print("Specific handler: invalid integer value")
    except ZeroDivisionError:
        print("Specific handler: division by zero")
    except Exception as error:
        # General handler is last because it can catch many exception types.
        print("General handler:", error)


process_value("hello")
process_value("zero")
process_value("-5")

# A non-specific (bare) except must also be the last handler.
# It catches errors that were not handled by the specific except blocks.
try:
    number = int("hello")
except ValueError:
    print("Specific except: invalid value")
except:
    print("Non-specific except: this is handled last")

# Avoid a bare `except:` in real programs when possible because it can hide
# the actual error. Prefer `except Exception as error` for general handling.


try:
    x=input("Please enter a number: ")
except ValueError as error:
    print("Exception handled:", error)

data = {'a':10,'b':20,'c':30,'d':15}
print(max(data,key=lambda x: data[x]))
'''grouping a liust of string based on theoir first letter'''


