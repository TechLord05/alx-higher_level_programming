#!/usr/bin/python3
"""
module function that adds a new attribute to an object if it’s possible
"""


def add_attribute(object, attrib_name, attrib_value):
    """function that adds a new attribute to an object if it’s possible

    Args:
        obj: The object to which the attribute will be added.
        name: The name of the new attribute.
        value: The value of the new attribute.

    Raises:
        TypeError: If the object can't have a new attribute.
    """
    if hasattr(object, '__dict__') or (hasattr(type(object), '__slots__') and
                                       attrib_name in type(object).__slots__):
        setattr(object, attrib_name, attrib_value)
    else:
        raise TypeError("can't add new attribute")
