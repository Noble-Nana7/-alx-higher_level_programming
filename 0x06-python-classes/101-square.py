#!/usr/bin/python3

"""
This module defines a class Square that represents a square
with attributes for size and position.
"""


class Square:
	"""
	A class to define a square with size and position attributes.
	"""

	def __init__(self, size=0, position=(0, 0)):
		"""
		Initializes a new Square instance.

		Arguments:
		size -- The size of the square (default is 0).
		position -- A tuple of 2 positive integers (default is (0, 0)).

		Raises:
		TypeError -- If size is not an integer or position is invalid.
		ValueError -- If size is less than 0.
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
		if (
			not isinstance(value, tuple) or
			len(value) != 2 or
			not all(isinstance(num, int) and num >= 0 for num in value)
		):
			raise TypeError("position must be a tuple of 2 positive integers")
		self.__position = value

	def area(self):
		"""
		Calculates and returns the area of the square.

		Returns:
		int -- The area of the square (size * size).
		"""
		return self.__size ** 2

	def my_print(self):
		"""
		Prints the square with the character # to stdout.
		If size is 0, prints an empty line.
		"""
		if self.__size == 0:
			print("")
			return

		# Print empty lines for vertical position
		print("\n" * self.__position[1], end="")

		# Print the square
		for _ in range(self.__size):
			print(" " * self.__position[0] + "#" * self.__size)

	def __str__(self):
		"""
		Defines the string representation of the square.

		Returns:
		str -- The square represented using the my_print method.
		"""
		if self.__size == 0:
			return ""

		result = []
		# Add empty lines for vertical position
		result.append("\n" * self.__position[1])

		# Add the square rows
		for _ in range(self.__size):
			result.append(" " * self.__position[0] + "#" * self.__size)

		return "\n".join(result)


if __name__ == "__main__":
	"""
	Main entry point for script execution.
	"""
	sq = Square(3, (1, 2))
	print(sq)
