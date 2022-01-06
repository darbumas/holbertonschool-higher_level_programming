#!/usr/bin/python3
def no_c(my_string):
    alt_str = ''
    for char in my_string:
        if char != 'c' and char != 'C':
            alt_str += char
    return alt_str
