#!/usr/bin/python3
"""
Defines a class MyList which inherits from list
"""


class MyList(list):
    """
    Class which uses a public instance method
    to print a sorted list from an existing list
    """

    def print_sorted(self):
        print("{}".format(sorted(self)))
