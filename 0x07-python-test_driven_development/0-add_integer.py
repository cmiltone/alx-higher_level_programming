#!/usr/bin/python3
"""
This is a simple integer addition module


"""


def add_integer(a, b=98):
    """
    Adds two integer
    """
    if isinstance(a, bool):
        raise TypeError("a must be an integer")
    if isinstance(b, bool):
        raise TypeError("b must be an integer")
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
