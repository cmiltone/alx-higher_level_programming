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
    l = 0
    for i in range(0, len(matrix)):
        if l != 0 and len(matrix[i]) != l:
            raise TypeError("Each row of the matrix must have the same size")
        new_matrix.append([])
        # new_matrix[i] = []
        for j in range(0, len(matrix[i])):
            if not isinstance(matrix[i][j], int) and not isinstance(matrix[i][j], float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_matrix[i].append(round(matrix[i][j] / div, 2))
        l = len(matrix[i])
    return new_matrix
