#!/usr/bin/python3
import random
number = random.randint(-10, 10)

if number < 0:
    msg = "is negative"
elif number > 0:
    msg = "is positive"
else:
    msg = "is zero"

print("{} {}".format(number, msg))
