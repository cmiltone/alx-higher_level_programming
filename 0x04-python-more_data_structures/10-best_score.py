#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    score = -100000000000
    key = ""
    for k in a_dictionary:
        if score < a_dictionary[k]:
            score = a_dictionary[k]
            key = k
    return key
