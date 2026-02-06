#!/usr/bin/python3
"""
Defines a class Rectangle that inherits BaseGeometry (7-base_geometry.py).
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Defines the class Rectangle
    """
    def __init__(self, width, height):
        """
        Initializes the Rectangle class with validated width and height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
