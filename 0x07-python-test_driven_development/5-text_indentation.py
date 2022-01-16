#!/usr/bin/python3
"""Module defines a function ``text_indentation(text)`` which prints a text with
2 new lines after each of these characters: . ? and :
The argument (text) has to be a string, otherwise raise a TypeError exception
message.
"""


def text_indentation(text):
    """prints `text` with two new lines after each of these: . ? :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    n_line = 1
    for char in text:
        if not (n_line and char == " "):
            print(char, end="")
            n_line = 0
            if char in '.?:':
                print('\n')
                n_line = 1
