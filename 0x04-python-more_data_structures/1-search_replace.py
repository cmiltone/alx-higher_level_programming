#!/usr/bin/python3
def search_replace(my_list, search, replace):
    k = 0
    new_list = []
    for i in my_list:
        if i == search:
            new_list.append(replace)
        else:
            new_list.append(i)
        k += 1
    return new_list
