#!/usr/bin/python3
"""This module creates a new class Square"""


class Square:
    """class 'Square' is instatiated with a private instance
    attribute: '_size"""
    def __init__(self, size=None):
        self.__size = size
