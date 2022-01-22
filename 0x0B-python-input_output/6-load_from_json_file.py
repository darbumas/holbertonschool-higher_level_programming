#!/usr/bin/python3
"""Module defines a ƒ() that creates an object from a JSON file"""

import json


def load_from_json_file(filename):
    """Creates an object from a JSON formated file."""
    with open(filename) as MyFile:
        return json.load(MyFile)
