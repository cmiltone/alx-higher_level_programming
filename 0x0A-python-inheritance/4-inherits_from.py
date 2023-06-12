#!/usr/bin/python3
""" module to check if the object is an instance of
a class that inherited (directly or indirectly)
from the specified class
"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of
    a class that inherited (directly or indirectly)
    from the specified class or False otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
