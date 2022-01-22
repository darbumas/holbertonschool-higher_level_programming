#!/usr/bin/python3
"""Module creates a class ``Student``"""


class Student:
    """Class with public attributes:
        1. first_name
        2. last_name
        3. age
        4. to_json(self)
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of the class instance."""
        return self.__dict__
