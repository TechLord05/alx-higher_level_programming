#!/usr/bin/python3
""" module function is_kind_of_class """


def inherits_from(obj, a_class):
    """Method that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False """
    obj_class = obj.__class__
    if obj_class == a_class:
        return (False)

    if issubclass(obj_class, a_class):
        return (True)
    for base_class in obj_class.__bases__:
        if inherits_from(base_class(), a_class):
            return (True)
    return (False)
