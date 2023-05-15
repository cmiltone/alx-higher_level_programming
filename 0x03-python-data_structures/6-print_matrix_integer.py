#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) == 0:
        print("".format())
    for i in range(0, len(matrix)):
        row = matrix[i]
        for j in range(0, len(row)):
            col = row[j]
            if j < len(row) - 1:
                print("{:d}".format(col), end=" ")
            else:
                print("{:d}".format(col))
