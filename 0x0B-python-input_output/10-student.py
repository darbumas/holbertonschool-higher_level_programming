#!/usr/bin/python3
"""Module creates a class ``Student``"""


from configparser import NoOptionError


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

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of the class instance."""
        if attrs is None:
            return self.__dict__
        attributes = {}
        for key, val in self.__dict__.items():
            if key in attrs:
                attributes[key] = val
        return attributes
