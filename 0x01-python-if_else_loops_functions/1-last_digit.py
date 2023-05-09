#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = int(repr(number)[-1])
if number < 0:
    ld = ld * -1
print(f'Last digit of {number} is {ld}', end = " ")
if ld > 5:
    print('and is greater than 5')
elif ld == 0:
    print(f'and is 0')
elif ld < 6:
    print('and is less than 6 and not 0')
