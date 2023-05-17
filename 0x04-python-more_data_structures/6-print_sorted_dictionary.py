#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = []
    for key in a_dictionary:
        keys.append(key)
    keys = sorted(keys)
    for k in keys:
        print("{}: {}".format(k, a_dictionary[k]))
