#!/usr/bin/python3
upper = [chr(x) for x in range(90, 64, -1)]
lower = [chr(x) for x in range(122, 96, -1)]

for i in range(0, 26, 1):
    if i % 2 != 0:
        print(upper[i], end="")
    else:
        print(lower[i], end="")
