#!/usr/bin/env python3

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: adds two numbers without using class or instance data."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: prints class attribute and multiplies two numbers."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
