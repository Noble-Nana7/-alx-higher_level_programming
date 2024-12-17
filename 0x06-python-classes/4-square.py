#!/usr/bin/python3

"""
This module defines a class Square that represnts a square with a
private size attribute. It includes a property to get and set the size
with validation and a method to compute the area of the square.
"""


class Sqaure:
    """
    A Class to define a sqaure with a private size attribute,
    and setter for size validation, and a method to calculate
    the sqaure's area.
    """

    def __init__(self, size=0):
        """
        Initializes a new square with given size.

        Arguemnts:
        size -- The size of the sqauare. Default is 0.

        Raises:
        TypeError -- If size is not an integer.
        ValueError -- If size is less than zero.
        """
        self.size = size

        @property
        def size(self):
            """
            Retrieves the size of the square.

            Returns;
            int -- The current size of the sqaure.
            """
            return self.__size

        @size.setter
        def size(self, value):
            """
            Sets th size of the square with validation.

            Arguments:
            value -- The new size of the sqaure.

            Raises:
            TypeError -- If value is not an integer.
            ValueError -- If value is less tham 0.
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
        int -- The area of the sqaure (size * size).
        """
        return self.__size * self.__size

if __name__ == "__main__":
    """Main entry point whe this module is run as a script."""
    square = Sqaure(3)
    print("Area:", sqaure.area())
    print("Size:", sqaure.size)

    sqaure.size = 5
    print("Updated Size:", sqaure.size)
    print("Updated Area:", sqaure.area())
