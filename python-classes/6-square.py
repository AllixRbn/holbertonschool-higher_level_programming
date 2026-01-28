#!/usr/bin/python3

"""
Class Square that defines a square by:

Private instance attribute: size:

property def size(self): to retrieve it

property setter def size(self, value): to set it:

If size is not an integer raise a TypeError exception with the message
size must be an integer

If size is less than 0, raise a ValueError exception with the message
size must be >= 0

Instantiation with optional size: def __init__(self, size=0):

Public instance method: def area(self):
returns the current square area
"""


class Square:
    """
    Defines a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the size of the square and its position
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Returns the size of the Square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with a private attribute
        Checks for value and type errors of size
        Raises TypeError: if size is not an integer
        Raises ValueError: if size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Returns the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets position with a private attribute
        Checks for value and type errors
        Raises TypeError: if position is not a tuple of 2 positive integers
        """
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Returns the area of the square
        """
        square_area = self.__size * self.__size
        return square_area

    def my_print(self):
        """
        Prints a square with # based on the given value

        If size is equal to 0, prints an empty line
        """
        if self.size == 0:
            print()
            return
        for i in range(self.position[1]):
            print()
        for i in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
