#!/usr/bin/python3
def roman_to_int(roman_string):
    my_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_value = 0
    if roman_string and type(roman_string) is str:
        letter_list = list(my_dict[i] for i in roman_string)
        last_letter = 0
        for i in range(0, len(letter_list)):
            if last_letter != 0 and last_letter < letter_list[i]:
                int_value += letter_list[i] - (last_letter * 2)
            else:
                int_value += letter_list[i]
                last_letter = letter_list[i]
    return int_value
