#!/usr/bin/python3
"""
Defines a function to read a text file and print its content
"""


def read_file(filename=""):
    """
    Reads a text file and prints its content
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())
