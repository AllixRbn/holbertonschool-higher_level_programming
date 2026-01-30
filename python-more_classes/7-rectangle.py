#!/usr/bin/python3
"""
Defines a rectangle
"""


class Rectangle:
    """
    Class Rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Defines the width and height of a rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Returns the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle with a private attribute
        Checks for value and type errors of width
        Raises TypeError: if width is not an integer
        Raises ValueError: if width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Returns the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle with a private attribute
        Checks for value and type errors of height
        Raises TypeError: if height is not an integer
        Raises ValueError: if height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the area of the rectangle
        """
        rectangle_area = self.__width * self.__height
        return rectangle_area

    def perimeter(self):
        """
        Returns the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            rectangle_perimeter = 0
        else:
            rectangle_perimeter = (self.__width * 2) + (self.__height * 2)
        return rectangle_perimeter

    def __str__(self):
        """
        Returns a printable reprensation of the rectangle with the
        value stored in print_symbol
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = ""
        print_symbol = str(self.print_symbol)
        for i in range(self.__height):
            rectangle += (print_symbol * self.__width)
            if i != self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """
        Returns a string representation of the rectangle
        to be able to recreate a new instance
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Print the message Bye rectangle...
        when an instance of Rectangle is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
