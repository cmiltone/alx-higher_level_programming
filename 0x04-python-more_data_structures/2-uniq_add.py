#!/usr/bin/python3
def uniq_add(my_list=[]):
    fianl_list = []
    sum_ = 0
    for i in my_list:
        if i not in fianl_list:
            fianl_list.append(i)
            sum_ += i
    return sum_
