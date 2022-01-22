#!/usr/bin/python3
"""Module defines a ƒ() that writes (appending) to a file,
and returns the number of characters added."""


def append_write(filename="", text=""):
    """Writes to a file (by appending), and returns number of characters
    added."""
    with open(filename, mode="a", encoding="utf-8") as MyFile:
        return MyFile.write(text)
