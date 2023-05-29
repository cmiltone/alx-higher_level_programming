#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value), end="\n")
        return True
    except ValueError:
        # print("".format(), end="")
        return False
