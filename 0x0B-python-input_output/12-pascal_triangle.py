#!/usr/bin/python3
"""Module defines a ƒ() that returns a list of lists of integers
representing the Pascal's triangle of n"""


def pascal_triangle(n):
    """Returns a list of lists of Pascal's triangle of n"""
    aList = []
    if n > 0:
        for i in range(1, n + 1):
            val = 1
            bList = []
            for d in range(1, i + 1):
                bList.append(str(val))
                val = val * (i - d) // d
            aList.append(bList)
    return aList
