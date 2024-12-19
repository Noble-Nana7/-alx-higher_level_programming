#!/usr/bin/python3

"""
This module defines a Node class for a singly linked list
and a SinglyLinkedList class to manage the linked list.
"""


class Node:
	"""
	A class to define a node of a singly linked list.
	"""

	def __init__(self, data, next_node=None):
		"""
		Initializes a new Node.

		Arguments:
		data -- The integer value of the node.
		next_node -- The next Node or None. Default is None.

		Raises:
		TypeError -- If data is not an integer or next_node is not a Node or None.
		"""
		self.data = data
		self.next_node = next_node

	@property
	def data(self):
		"""
		Retrieves the data stored in the node.

		Returns:
		int -- The data value of the node.
		"""
		return self.__data

	@data.setter
	def data(self, value):
		"""
		Sets the data value of the node with validation.

		Arguments:
		value -- The new data value (must be an integer).

		Raises:
		TypeError -- If value is not an integer.
		"""
		if not isinstance(value, int):
			raise TypeError("data must be an integer")
		self.__data = value

	@property
	def next_node(self):
		"""
		Retrieves the next node.

		Returns:
		Node or None -- The next node or None if there's no next node.
		"""
		return self.__next_node

	@next_node.setter
	def next_node(self, value):
		"""
		Sets the next node with validation.

		Arguments:
		value -- The next node (must be a Node or None).

		Raises:
		TypeError -- If value is not a Node or None.
		"""
		if value is not None and not isinstance(value, Node):
			raise TypeError("next_node must be a Node object")
		self.__next_node = value


class SinglyLinkedList:
	"""
	A class to define a singly linked list.
	"""

	def __init__(self):
		"""
		Initializes a new singly linked list.
		"""
		self.__head = None

	def __str__(self):
		"""
		Defines the string representation of the linked list.

		Returns:
		str -- A string of node data separated by new lines.
		"""
		nodes = []
		current = self.__head
		while current:
			nodes.append(str(current.data))
			current = current.next_node
		return "\n".join(nodes)

	def sorted_insert(self, value):
		"""
		Inserts a new Node with a given value in sorted order.

		Arguments:
		value -- The value of the new node.
		"""
		new_node = Node(value)
		if self.__head is None or self.__head.data >= value:
			new_node.next_node = self.__head
			self.__head = new_node
		else:
			current = self.__head
			while current.next_node and current.next_node.data < value:
				current = current.next_node
			new_node.next_node = current.next_node
			current.next_node = new_node


if __name__ == "__main__":
	"""
	Main entry point when this module is run as a script.
	"""
	sll = SinglyLinkedList()
	sll.sorted_insert(3)
	sll.sorted_insert(1)
	sll.sorted_insert(2)
	sll.sorted_insert(5)
	print(sll)
