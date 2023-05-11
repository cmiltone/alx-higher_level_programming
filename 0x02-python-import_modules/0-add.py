#!/usr/bin/python3
func = __import__('add_0').add
a = 1
b = 2
print('{} + {} = {}'.format(a, b, func(a, b)))
