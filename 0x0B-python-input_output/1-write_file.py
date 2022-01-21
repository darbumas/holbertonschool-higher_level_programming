#!/usr/bin/python3
"""Module defines a ƒ() to write a string to a file and returns
number of characters written."""


def write_file(filename="", text=""):
    """Returns number of characters written to a file."""
    with open(filename, mode='w', encoding='utf-8') as MyFile:
        return MyFile.write(text)
