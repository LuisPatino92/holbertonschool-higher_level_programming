#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    numerator = int()
    denominator = int()
    for element in my_list:
        numerator += element[0] * element[1]
        denominator += element[1]
    return float(numerator)/float(denominator)
