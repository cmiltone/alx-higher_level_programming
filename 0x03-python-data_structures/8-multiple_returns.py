#!/usr/bin/python3
def multiple_returns(sentence):
    a = len(sentence)
    c = None
    if a > 0:
        c = sentence[0]
    return (a, c)
