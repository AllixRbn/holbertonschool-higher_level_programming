#!/usr/bin/python3


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

    def area(self):
        """
        Returns the are of the square
        """
        square_area = self.__size * self.__size
        return square_area
