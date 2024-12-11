#!/usr/bin/python3

"""
This module defines a class Square that represents a square with a private 
size attribute. The size is used to define the square and is kept private 
for future control and validation of its value.
"""

class Square:
    """
    A class to define a square with a private size attribute.
    """

    def __init__(self, size):
        """
        Initializes a new Square with a given size.

        Arguments:
        size -- The size of the square.
        """
        self.__size = size


if __name__ == "__main__":
    """Main entry point when this module is run as a script."""
    square = Square(5)
