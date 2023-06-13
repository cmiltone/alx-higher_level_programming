#!/usr/bin/python3
"""module that gets pascal's triangle"""


def pascal_triangle(n):
    """returns pascal's triangle"""
    if n <= 0:
        return []
    triangle = []
    for i in range(1, n + 1):
        k = 1
        t = []
        for j in range(1, i + 1):
            t.append(k)
            k = k * (i - j) // j binomial coefficient
        triangle.append(t)
    return triangle
