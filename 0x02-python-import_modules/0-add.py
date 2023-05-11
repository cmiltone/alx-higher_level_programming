#!/usr/bin/python3
import sys
if __name__ == "__main__":
    add = __import__('add_0').add
    a = 1
    b = 2
    print('{} + {} = {}'.format(a, b, add(a, b)))
    sys.exit(0)
