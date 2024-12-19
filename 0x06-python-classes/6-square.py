#!/usr/bin/python3

"""
This module defines a class Square that represents a square with
a size, position, and methods to calculate area and print the square.
"""


class Square:
    """
    A class to define a square with size, position, and additional methods.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new square with given size and position.

        Arguments:
        size -- The size of the square. Default is 0.
        position -- A tuple containing the square's position. Default is (0, 0).

        Raises:
        TypeError -- If size is not an integer or position is not a tuple of 2 positive integers.
        ValueError -- If size is less than zero.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
        tuple -- The current position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square with validation.

        Arguments:
        value -- A tuple of 2 positive integers.

        Raises:
        TypeError -- If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
        int -- The area of the square (size * size).
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square with the character '#' based on size and position.

        If size is equal to 0, an empty line is printed.
        """
        if self.__size == 0:
            print("")
            return

        # Print position[1] new lines (top margin)
        for _ in range(self.__position[1]):
            print("")

        # Print the square rows
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)


if __name__ == "__main__":
    """
    Main entry point when this module is run as a script.
    """
    my_square = Square(5, (2, 3))
    my_square.my_print()

    print("--")

    my_square.size = 3
    my_square.position = (1, 1)
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()
