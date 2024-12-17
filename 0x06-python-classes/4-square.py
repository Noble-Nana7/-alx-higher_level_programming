#!/usr/bin/python3

"""
This module defines a class Square that represents a square with a
private size attribute. It includes a property to get and set the size
with validation and a method to compute the area of the square.
"""


class Square:
    """
    A Class to define a square with a private size attribute,
    and setter for size validation, and a method to calculate
    the square's area.
    """

    def __init__(self, size=0):
        """
        Initializes a new square with given size.

        Arguments:
        size -- The size of the square. Default is 0.

        Raises:
        TypeError -- If size is not an integer.
        ValueError -- If size is less than zero.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
        int -- The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.

        Arguments:
        value -- The new size of the square.

        Raises:
        TypeError -- If value is not an integer.
        ValueError -- If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
        int -- The area of the square (size * size).
        """
        return self.__size * self.__size


if __name__ == "__main__":
    """Main entry point when this module is run as a script."""
    square = Square(3)
    print("Area:", square.area())
    print("Size:", square.size)

    square.size = 5
    print("Updated Size:", square.size)
    print("Updated Area:", square.area())
