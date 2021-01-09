#!/usr/bin/python3
"""This module only has the matrix divided function"""


def matrix_divided(matrix, div):
    """ Take a matrix and return a matrix of the same size, but with
        all the elemets divided by div.

    Args:
        matrix:     List of lists with all the rows of same length.
        div:        An int or Float, diferent than 0.

    Returns:
        A matrix of exactli same size as the input, but with each element
        divided by div, rounded to 2 decimal places.
    """

    # div quality checking
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Checking quality of matrix, and computing divided matrix
    standard_length = 0
    divided_matrix = []

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    if isinstance(matrix[0], list):
            standard_length = len(matrix[0])

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
        if len(row) != standard_length:
            raise TypeError("Each row of the matrix must have the same size")
        divided_row = []
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
            divided_row.append(round(element/div, 2))
        divided_matrix.append(divided_row)
    return divided_matrix

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
