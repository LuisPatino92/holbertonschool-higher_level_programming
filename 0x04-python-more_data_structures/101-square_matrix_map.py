#!/usr/bin/python3
def square_matrix_map(m=[]):
    return list(map(lambda e: list(map(lambda n: n ** 2, e)), m))
