#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        max_val = my_list[0]
        for digit in my_list:
            if max_val < digit:
                max_val = digit
        return max_val
