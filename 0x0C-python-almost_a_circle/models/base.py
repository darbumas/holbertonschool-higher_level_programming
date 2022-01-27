#!/usr/bin/python3
"""Module creates a class ``Base``."""

import json


class Base:
    """Class is the base of all other classes in this project.
    With private class attribute:   __nb_objects = 0
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method returns a JSON string representation of
        its' argument"""
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
