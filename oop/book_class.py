#!/usr/bin/env python3
"""
A Book class demonstrating Python magic methods:
- __init__
- __del__
- __str__
- __repr__
"""

class Book:
    """Represents a book with title, author, and publication year."""

    def __init__(self, title, author, year):
        """Constructor that initializes the book attributes."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor that announces when a Book instance is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """User-friendly string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation that can recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
