#!/usr/bin/python3
"""Module defines a ƒ() that reaturns a JSON representation of a string."""

import json


def to_json_string(my_obj):
    """Returns a JSON representation of a string"""
    return json.dumps(my_obj)
