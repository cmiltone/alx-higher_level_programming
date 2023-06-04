#!/usr/bin/python3
"""
This is a simple matrix division module


"""


def matrix_divided(matrix, div):
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    k = 0
    s1 = "matrix must be a matrix (list of lists) of integers/floats"
    for i in range(0, len(matrix)):
        if k != 0 and len(matrix[i]) != k:
            raise TypeError("Each row of the matrix must have the same size")
        new_matrix.append([])
        # new_matrix[i] = []
        for j in range(0, len(matrix[i])):
            isint = isinstance(matrix[i][j], int)
            isfloat = isinstance(matrix[i][j], float)
            if not isint and not isfloat:
                raise TypeError(s1)
            new_matrix[i].append(round(matrix[i][j] / div, 2))
        k = len(matrix[i])
    return new_matrix
