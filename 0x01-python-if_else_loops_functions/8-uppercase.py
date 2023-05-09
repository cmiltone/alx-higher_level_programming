#!/usr/bin/python3
def uppercase(c):
    s = ""
    for k in c:
        i = ord(k)
        if i >= 97 and i <= 122:
            i = i - 32
            s = s + chr(i)
        else:
            s = s + k
    print(s)
