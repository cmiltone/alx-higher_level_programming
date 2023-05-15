#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = []
    for i in my_list:
        if i != idx:
            new_list.append(i)
    my_list = new_list
    return my_list
