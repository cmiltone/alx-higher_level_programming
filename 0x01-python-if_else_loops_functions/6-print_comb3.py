#!/usr/bin/python3
for i in range(0,9):
    for j in range(1, 10):
        if (i != j and j > i):
            if j + i != 17:
                print("{}{}".format(i, j), end=", ")
            else:
                print("{}{}".format(i, j))
