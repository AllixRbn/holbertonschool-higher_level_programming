#!/usr/bin/python3
"""
Defines an abstract class named Shape with two abstract methods:
area and perimeter
Implement two concrete classes: Circle and Rectangle, both inheriting Shape
"""


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for shapes
    """

    @abstractmethod
    def area(self):
        """
        Calculates the area of the shape
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculates the perimeter of the shape
        """
        pass


class Circle(Shape):
    """
    Circle shape
    """

    def __init__(self, radius):
        """
        Initializes a Circle with a given radius
        """
        self.radius = radius

    def area(self):
        """
        Calculates the area of the circle
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Calculates the circumference of the circle
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle shape
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle with a given width and height
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculates the area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints area and perimeter of any object
    that provides area() and perimeter() methods
    (duck typing)
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
