#!/usr/bin/python3
import sys

calc = __import__('calculator_1')
a = 10
b = 5
print('{} + {} = {}'.format(a, b, calc.add(a, b)))
print('{} - {} = {}'.format(a, b, calc.sub(a, b)))
print('{} * {} = {}'.format(a, b, calc.mul(a, b)))
print('{} / {} = {}'.format(a, b, calc.div(a, b)))

if __name__ == "__main__":
    sys.exit(0)
