#!/usr/bin/python3
import sys
def func():
    add = __import__('add_0').add
    a = 1
    b = 2
    print('{} + {} = {}'.format(a, b, add(a, b)))

if __name__ == "__main__":
    func()
    sys.exit(0)
