#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n = 0
    try:
        while n < x:
            print("{}".format(my_list[n]), end="")
            n += 1
    except IndexError:
        print("".format(), end="")
    finally:
        print("".format())
    return n
