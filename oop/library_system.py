#!/usr/bin/env python3

class Book:
    """Base class representing a book with a title and author."""

    def __init__(self, title: str, author: str):
        """Initialize the Book with a title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Represents a digital book (EBook), inheriting from Book."""

    def __init__(self, title: str, author: str, file_size: int):
        """
        Initialize EBook with title, author, and file size in KB.
        Calls the parent class initializer.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Represents a physical print book, inheriting from Book."""

    def __init__(self, title: str, author: str, page_count: int):
        """
        Initialize PrintBook with title, author, and page count.
        Calls the parent class initializer.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Represents a library containing different types of books."""

    def __init__(self):
        """Initialize the Library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook instance to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of each book in the library."""
        for book in self.books:
            print(book)
