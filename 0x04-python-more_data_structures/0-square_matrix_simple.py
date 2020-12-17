#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []
    i = 0
    for row in matrix:
        squared_matrix += [[]]
        for column in row:
            squared_matrix[i] += [column ** 2]
        i += 1
    return squared_matrix
