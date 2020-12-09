#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number != 0:
    last = int((number/abs(number)) * (abs(number) % 10))
else:
    last = 0

if last > 5:
    msg = "and is greater than 5"
elif last < 6 and last != 0:
    msg = "and is less than 6 and not 0"
else:
    msg = "and is 0"

print("Last digit of {} is {} {}".format(number, last, msg))
