#!/usr/bin/python3
"""
Define a class CountedIterator
"""


class CountedIterator:
    """
    Iterator that counts how many items have been iterated over
    """

    def __init__(self, iterable):
        """
        Initialize the CountedIterator with an iterable
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """
        Return the next item from the iterator and increment the count
        """
        item = next(self.iterator)   # may raise StopIteration
        self.count += 1
        return item

    def get_count(self):
        """
        Return the number of items that have been iterated over
        """
        return self.count
