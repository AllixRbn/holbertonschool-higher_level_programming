#!/usr/bin/python3
"""
Defines a class Student
"""


class Student:
    """
    Student class with public attributes first_name, last_name and age
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes the Student class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance
        If attrs is a list of strings, only attribute
        names contained in this list must be retrieved
        """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    new_dict[attr] = getattr(self, attr)
            return new_dict
