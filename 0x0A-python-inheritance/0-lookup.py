#!/usr/bin/python3
"""
This module defines the lookup function, which returns a list of available
attributes and methods of an object.
"""


def lookup(obj):
    """Returns list of methods (runs dir())."""
    return dir(obj)
