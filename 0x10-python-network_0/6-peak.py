#!/usr/bin/python3
"""module defines a function that
finds a p in a list of unsorted integers"""


def find_p(list_of_integers):
    """finds a p in a list of unsorted integers"""
    if list_of_integers == []:
        return None

    n = len(list_of_integers)
    if n == 1:
        return list_of_integers[0]
    elif n == 2:
        return max(list_of_integers)

    m = int(n / 2)
    p = list_of_integers[m]
    if p > list_of_integers[m - 1] and p > list_of_integers[m + 1]:
        return p
    elif p < list_of_integers[m - 1]:
        return find_p(list_of_integers[:m])
    else:
        return find_p(list_of_integers[m + 1:])
