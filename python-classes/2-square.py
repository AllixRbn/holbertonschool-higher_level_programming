#!/usr/bin/python3

"""
Class Square that defines a square by:

Private instance attribute: size

Instantiation with optional size: def __init__(self, size=0):

size must be an integer, otherwise raise a TypeError exception with the message
size must be an integer
if size is less than 0, raise a ValueError exception with the message
size must be >= 0
"""


class Square:
    """
    Defines a square

    args:
    - size: defines the size of the square
    """
    def __init__(self, size=0):
        """
        Initializes the square with a private size given by user
        Checks for value and type errors of size
        Raises TypeError: if size is not an integer
        Raises ValueError: if size is less than 0
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
