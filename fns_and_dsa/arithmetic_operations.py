#!/usr/bin/env python3
"""
This module defines a function to perform basic arithmetic operations.
"""

def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform a basic arithmetic operation on two numbers.

    Parameters:
        num1 (float): First number.
        num2 (float): Second number.
        operation (str): Operation type - "add", "subtract", "multiply", "divide".

    Returns:
        float or str: Result of the arithmetic operation, or an error message.
    """

    if operation == "add":
        return num1 + num2

    elif operation == "subtract":
        return num1 - num2

    elif operation == "multiply":
        return num1 * num2

    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2

    else:
        return "Error: Invalid operation. Choose add, subtract, multiply, or divide."
