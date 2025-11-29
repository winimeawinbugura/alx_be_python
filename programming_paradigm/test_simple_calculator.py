#!/usr/bin/env python3
"""
Unit tests for the SimpleCalculator class.
"""

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Test suite for SimpleCalculator."""

    def setUp(self):
        """Create a calculator instance before each test."""
        self.calc = SimpleCalculator()

    # ---------------------- ADDITION TESTS ----------------------
    def test_addition_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_addition_negative_numbers(self):
        self.assertEqual(self.calc.add(-5, -7), -12)

    def test_addition_mixed_numbers(self):
        self.assertEqual(self.calc.add(-1, 4), 3)

    def test_addition_with_zero(self):
        self.assertEqual(self.calc.add(10, 0), 10)

    # ---------------------- SUBTRACTION TESTS ----------------------
    def test_subtraction_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)

    def test_subtraction_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-5, -2), -3)

    def test_subtraction_mixed_numbers(self):
        self.assertEqual(self.calc.subtract(3, -3), 6)

    def test_subtraction_with_zero(self):
        self.assertEqual(self.calc.subtract(9, 0), 9)

    # ---------------------- MULTIPLICATION TESTS ----------------------
    def test_multiplication_positive_numbers(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)

    def test_multiplication_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-4, -3), 12)

    def test_multiplication_mixed_numbers(self):
        self.assertEqual(self.calc.multiply(-3, 6), -18)

    def test_multiplication_with_zero(self):
        self.assertEqual(self.calc.multiply(10, 0), 0)

    # ---------------------- DIVISION TESTS ----------------------
    def test_division_normal(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_division_float_result(self):
        self.assertEqual(self.calc.divide(7, 2), 3.5)

    def test_division_negative_numbers(self):
        self.assertEqual(self.calc.divide(-8, -2), 4)

    def test_division_mixed_numbers(self):
        self.assertEqual(self.calc.divide(9, -3), -3)

    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))

if __name__ == "__main__":
    unittest.main()
