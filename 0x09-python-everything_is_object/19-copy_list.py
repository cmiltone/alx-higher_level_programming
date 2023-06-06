#!/usr/bin/python3
def copy_list(a):
    return a[:] if (isinstance(a, tuple) or isinstance(a, list) or isinstance(a, str)) else a
