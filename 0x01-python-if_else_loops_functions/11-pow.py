#!/usr/bin/python3
def pow(a, b):
    if a == 0 or a == 1 or b == 1:
        return a
    if a == -1:
        if b % 2 == 0:
            return 1
        else:
            return -1
    if b == 0:
        return 1
    if b < 0:
        return 1 / pow(a, -b)
    k = pow(a, b//2)
    if b % 2 == 0:
        return k * k
    return k * k * a
