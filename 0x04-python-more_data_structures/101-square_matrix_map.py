#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new_list = list(map(lambda element:
                    list(map(lambda num: num ** 2, element)), matrix))
    return new_list
