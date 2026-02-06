#!/usr/bin/python3
"""
Defines an empty class BaseGeometry
"""


class BaseGeometry:
    """
    Base class for geometry
    """

    def area(self):
        """
        Raises an exception ebcause area is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value > 0 and an int
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
