#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diffs = []
    for i in set_1:
        if i not in set_2 and i not in diffs:
            diffs.append(i)
    for k in set_2:
        if k not in set_1 and k not in diffs:
            diffs.append(k)
    return diffs
