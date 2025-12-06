#!/usr/bin/env python3

import math


class Shape:
    """Base class for all shapes."""

    def area(self):
        """Method to be overridden by subclasses."""
        raise NotImplementedError("Subclasses must override this method.")


class Rectangle(Shape):
    """Rectangle shape with length and width."""

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculate area of a rectangle."""
        return self.length * self.width


class Circle(Shape):
    """Circle shape with radius."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate area of a circle."""
        return math.pi * (self.radius ** 2)
