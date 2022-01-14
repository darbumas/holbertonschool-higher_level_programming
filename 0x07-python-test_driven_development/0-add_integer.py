#!/usr/bin/python3
""" This module defines a function with two parameter arguments.
Calculates and returns the sum of its' integer (or floats) arguments.
"""


def add_integer(a, b=98):
    """ Returns the sum of a and b.
    Raises exceptions if a or b are neither ints nor floats
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
