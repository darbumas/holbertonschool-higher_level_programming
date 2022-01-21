#!/usr/bin/python3
"""Module creates a class ``Square`` derived from parent class ``Rectangle``"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class inherits from parent class ``Rectangle``"""
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
