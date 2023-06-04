#!/usr/bin/python3
"""
This is a simple module to multiply matrices using numpy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_a, list):
        raise TypeError("m_b must be a list")
    for a in range(0, len(m_a)):
        if not isinstance(m_a[a], list):
            raise TypeError("m_a must be a list of lists")
    for b in range(0, len(m_b)):
        if not isinstance(m_b[b], list):
            raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")
    i = 0
    j = 0
    y = len(m_a[0])
    z = len(m_b[0])
    for a in range(0, len(m_a)):
        if a != 0 and y != len(m_a[a]):
            raise TypeError("each row of m_a must be of the same size")
        for c in range(0, len(m_a[a])):
            isint = isinstance(m_a[a][c], int)
            isfloat = isinstance(m_a[a][c], float)
            if not isint and not isfloat:
                raise ValueError("m_a should contain only integers or floats")
        i += 1

    for b in range(0, len(m_b)):
        if b != 0 and z != len(m_b[b]):
            raise TypeError("each row of m_b must be of the same size")
        for d in range(0, len(m_b[b])):
            isint = isinstance(m_b[b][d], int)
            isfloat = isinstance(m_b[b][d], float)
            if not isint and not isfloat:
                raise ValueError("m_b should contain only integers or floats")
        j += 1

    return np.matmul(m_a, m_b)
