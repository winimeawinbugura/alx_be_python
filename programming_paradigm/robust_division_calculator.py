#!/usr/bin/env python3
"""
Robust division calculator with error handling.
"""

def safe_divide(numerator, denominator):
    """
    Safely divide two numbers with error handling.
    Handles:
    - Non-numeric input
    - Division by zero
    """

    try:
        num = float(numerator)
        den = float(denominator)

        try:
            result = num / den
            return f"The result of the division is {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."
