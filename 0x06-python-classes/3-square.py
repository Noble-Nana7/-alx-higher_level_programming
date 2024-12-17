#!/usr/bin/python3

"""
This module defines a class Square that represents a square with
a private size attribute and a method to compute its area. The size
is validated to ensure it is an integer and >= 0.
"""


class Square:
    """
    A class to define a square with a private size attribute and a method to
    compute the square's area.
    """

    def __init__(self, size=0):
        """
        Initializes a new Squaew with a given size.

        Arguments:
        size -- The size of the square. Default is 0.

        Raises:
        TypeError -- If size is not an integer.
        ValueError -- If size is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
        int - The area of the square (size * size).
        """
        return self.__size * self.__size

    if __name__ == "__main__":
        """ Main entry point when this module is run as a script."""
        square = Square(5)
        print("Area:", square.area())
