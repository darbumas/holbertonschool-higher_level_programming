#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        char = ord(letter)
        if char >= 97 and number <= 122:
            char -= 32
        print("{}".format(chr(char)), end="")
    print()
