#!/usr/bin/python3

"""
This module defines a class Square that represents a square
with private size, area computation, and square printing.
"""


class Square:
    """
    A Class to define a square with a private size attribute,
    and methods to compute the area and print the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new square with the given size.

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

    def my_print(self):
        """
        Prints the square using the character '#'.
        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("--")
        else:
            for i in range(self.__size):
                print("#" * self.__size)


if __name__ == "__main__":
    """Main entry point when this module is run as a script."""
    square = Square(3)
    square.my_print()

    print("Area:", square.area())

    square.size = 0
    square.my_print()

    square.size = 4
    square.my_print()
    print("Updated Area:", square.area())

