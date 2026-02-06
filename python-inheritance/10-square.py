#!/usr/bin/python3
"""
Defines a Square class
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Defines the Square class that inherits Rectangle
    """
    def __init__(self, size):
        """
        Initializes the Square class with validated size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
