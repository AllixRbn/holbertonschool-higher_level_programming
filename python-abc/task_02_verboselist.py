#!/usr/bin/env python3
"""
Defines a class named VerboseList that inherits the built-in list class
and overrides the append, extend, remove, and pop methods to print a message
"""


class VerboseList(list):
    """A list that prints notifications when modified"""

    def append(self, item):
        """
        Appends an item to the list and prints a message
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extends the list with an iterable and prints a message
        """
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """
        Removes an item from the list and prints a message
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Pops an item from the list at the specified index and prints a message
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
