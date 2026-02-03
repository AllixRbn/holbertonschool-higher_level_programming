#!/usr/bin/python3
"""
Defines a function that returns True if the object is exactly an instance
of the specified class or, otherwise, False
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance
    of the specified class
    """
    if type(obj) is a_class:
        return True
    return False
