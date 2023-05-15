#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_ = my_list[0]
    for i in my_list:
        if max_ < i:
            max_ = i
    return max_
