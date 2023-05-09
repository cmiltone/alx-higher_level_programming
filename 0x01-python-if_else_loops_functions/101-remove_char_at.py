#!/usr/bin/python3
def remove_char_at(str_, n):
    l = len(str_)
    s = ""
    i = 0

    for c in str_:
        if i != n:
            s = s + c
        i += 1
    return s
