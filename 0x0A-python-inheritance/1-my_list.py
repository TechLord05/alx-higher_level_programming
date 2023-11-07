#!/usr/bin/python3

"""
This module defines the MyList class, a custom list class that inherits from
the built-in list class. It provides an additional method to print the list
in a sorted manner.
"""


class MyList(list):
    """
    Custom list class that inherits from the built-in list class.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        print(sorted(self))
