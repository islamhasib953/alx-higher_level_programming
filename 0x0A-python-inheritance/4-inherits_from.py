#!/usr/bin/python3

"""4-inherits_from"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a
    class that inherited (directly or indirectly)"""
    return isinstance(obj, a_class) and type(obj) is not a_class
