#!/usr/bin/python3*
"""
Defines a function to append string to text file
Returns number of added characters
"""


def append_write(filename="", text=""):
    """
    Appends string to text file
    Returns number of added characters
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
