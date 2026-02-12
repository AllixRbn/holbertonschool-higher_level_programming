#!/usr/bin/python3
"""
Defines a function to write a string to a text file
Returns the number of written characters
"""


def write_file(filename="", text=""):
    """
    Writes string to text file
    Returns number of written characters
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
