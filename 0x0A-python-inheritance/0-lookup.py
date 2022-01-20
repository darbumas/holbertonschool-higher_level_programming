#!/usr/bin/python3
"""Module defines a ƒ() ``lookup(obj)`` that returns a list of objects."""


def lookup(obj):
    """Returns the list of available attributes and methods of an object"""
    return dir(obj)
