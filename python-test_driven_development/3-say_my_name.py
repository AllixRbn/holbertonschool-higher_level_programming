#!/usr/bin/python3
"""
Module 3-say_my_name
Provides 1 function:
say_my_name(first_name, last_name=""): prints a message with the given names
"""


def say_my_name(first_name, last_name=""):
    """
    prints My name is first_name last_name
    >>> say_my_name("John", "Smith")
    My name is John Smith
    >>> say_my_name("Walter", "White")
    My name is Walter White
    >>> say_my_name("Bob")
    My name is Bob
    >>> say_my_name(12, "White")
    Traceback (most recent call last):
    ...
    TypeError: first_name must be a string
    >>> say_my_name("Allix", 24)
    Traceback (most recent call last):
    ...
    TypeError: last_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
