#!/usr/bin/python3
""" Module defines a function ``print_square(size)`` with one argument.
The function prints a square with the character '#'. The argument (size)
has to be an integer, otherwise raise a TypeError exception message.
Also size has to be a positive value, otherwise raise a ValueError
exception message.
"""


def print_square(size):
    """ Prints a square with the character '#' if `size` is a positive integer"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
