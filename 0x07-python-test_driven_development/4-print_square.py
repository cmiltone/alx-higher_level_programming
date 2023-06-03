#!/usr/bin/python3
"""
This is a simple module to print a square with #


"""


def print_square(size):
    """
    prints a square with #
    """
    if isinstance(size, bool):
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print("\n".format())
    else:
        for i in range(0, size):
            for j in range(0, size):
                print("#".format(), end="")
            print("".format(), end="\n")
