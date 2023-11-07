#!/usr/bin/python3
"""Module containing a function to check if an object is an
instance or inherited instance of a specific class."""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance or inherited instance of a
    specified class.

    Args:
        obj (object): The object to be checked.
        a_class (type): The class to check against.

    Returns:
        bool: True if obj is an instance or inherited instance of a_class,
        False otherwise.
    """
    return isinstance(obj, a_class)
