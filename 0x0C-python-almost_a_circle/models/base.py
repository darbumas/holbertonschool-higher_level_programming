#!/usr/bin/python3
"""Module creates a class ``Base``."""

from os import path
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

    @classmethod
    def save_to_file(cls, list_objs):
        """class method that writes JSON string representation of list_objs
         to a file"""
        filename = cls.__name__ + ".json"
        obj_list = []
        if list_objs is not None:
            for obj in list_objs:
                obj_list.append(cls.to_dictionary(obj))
        with open(filename, mode="w", encoding="utf-8") as myFile:
            myFile.write(cls.to_json_string(obj_list))

    @staticmethod
    def from_json_string(json_string):
        """static method returns a list of the JSON string representation"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """class method returns a new instance of a class with all attributes
        already set"""
        if cls.__name__ == "Square":
            new_instance = cls(1)
        else:
            new_instance = cls(1, 1)
        cls.update(new_instance, **dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """class method returns a list of instances"""
        filename = cls.__name__ + ".json"
        inst_list = []
        if path.isfile(filename):
            with open(filename, mode="r", encoding="utf-8") as myFile:
                inst_list = cls.from_json_string(myFile.read())
            return [cls.create(**obj) for obj in inst_list]
        return inst_list
