#!/usr/bin/python3
"""This module creates a new class Square"""


class Square:
    """class 'Square' is instatiated with a private instance
    attribute: '_size"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Private attribute 'size' getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Private attribute 'size' setter"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Instance method returns the area of a 'Square' object"""
        return (self.__size * self.__size)
