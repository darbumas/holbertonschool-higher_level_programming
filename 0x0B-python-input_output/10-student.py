#!/usr/bin/python3
"""Module creates a class ``Student``"""


from configparser import NoOptionError
from webbrowser import get


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
        if isinstance(attrs, list):
            my_dict = {}
            for i in attrs:
                if hasattr(self, i):
                    my_dict[i] = getattr(self, i)
            return my_dict
        return self.__dict__
