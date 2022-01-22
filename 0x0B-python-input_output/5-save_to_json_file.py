#!/usr/bin/python3
"""Module defines a ƒ() that writes an object to a text file using
JSON representation"""

import json


def save_to_json_file(my_obj, filename):
    """Writes to a file a JSON representation of an object"""
    with open(filename, mode="w", encoding="utf-8") as MyFile:
        return MyFile.write(json.dumps(my_obj))
