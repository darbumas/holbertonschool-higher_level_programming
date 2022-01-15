#!/usr/bin/python3
""" Module defines a function ``matrix_divided()`` that takes two paramete
arguments. The first argument is a list of lists (matrix) of int/floats,
and the second argument is a divider of type int/float. ``matrix_divided``
returns a new matrix comprised of each element of the matrix divided by the
divider.
"""


def matrix_divided(matrix, div):
    """
    Returns a new matrix containing the results of the division of each
    element of the matrix by div.
    """

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    error = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(error)

    for row in matrix:
        if type(row) is not list or len(row) == 0:
            raise TypeError(error)
        for item in row:
            if type(item) is not int and type(item) is not float:
                raise TypeError(error)

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
