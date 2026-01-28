#!/usr/bin/python3

"""
Class Square that defines a square by:

Private instance attribute: size

Instantiation with size (no type/value verification)

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
        """
        self.__size = size
