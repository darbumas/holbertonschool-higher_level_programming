#!/usr/bin/python3
"""Module defines a ƒ() that returns a dictionary description with
simple data structure list for JSON serialization"""


def class_to_json(obj):
    """Returns a dictionary for JSON serialization"""
    return obj.__dict__
