#!/usr/bin/python3

"""
This module defines a class Square that represents a square with a private
size attributr. The size is validated to ensure it is an integer
and is >= 0.
"""


class Square:

    """
    A class to define a squre with a private size attribute,
    with validation for size input

    """

    def __init__(self, size=0):
        """
        Initializing a new squre with a give size.

        Arguements:
        size -- The size of the square. Default is 0

        Raises:
        TypeError -- If size is not an integer.
        ValueError -- If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size


if __name__ == "__main__":
    """ Main entry point when this module is run asa script"""
    square = Square(5)
