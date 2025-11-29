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

    # ---------------------- ADDITION TEST ----------------------
    def test_addition(self):
        """Test addition method with multiple cases."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-5, -7), -12)
        self.assertEqual(self.calc.add(-1, 4), 3)
        self.assertEqual(self.calc.add(10, 0), 10)

    # ---------------------- SUBTRACTION TEST ----------------------
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(-5, -2), -3)
        self.assertEqual(self.calc.subtract(3, -3), 6)
        self.assertEqual(self.calc.subtract(9, 0), 9)

    # ---------------------- MULTIPLICATION TEST ----------------------
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-4, -3), 12)
        self.assertEqual(self.calc.multiply(-3, 6), -18)
        self.assertEqual(self.calc.multiply(10, 0), 0)

    # ---------------------- DIVISION TEST ----------------------
    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        self.assertEqual(self.calc.divide(-8, -2), 4)
        self.assertEqual(self.calc.divide(9, -3), -3)
        self.assertIsNone(self.calc.divide(10, 0))

if __name__ == "__main__":
    unittest.main()
