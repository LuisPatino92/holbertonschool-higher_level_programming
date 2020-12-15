#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        i = 0
        for num in row:
            i += 1
            if i == len(row):
                print("{:d}".format(num))
            else:
                print("{:d}".format(num), end=" ")
    if len(matrix[0]) == 0:
        print("")
