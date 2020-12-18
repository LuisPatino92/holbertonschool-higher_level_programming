#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    rti = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    for letter in roman_string:
        if letter not in rti:
            return 0
    num = int(0)

    for i in range(len(roman_string)):
        num += int(rti[roman_string[i]])
        if i > 0 and int(rti[roman_string[i - 1]]) < int(rti[roman_string[i]]):
            num -= 2 * (int(rti[roman_string[i - 1]]))
    return num
