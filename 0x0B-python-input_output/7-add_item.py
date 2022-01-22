#!/usr/bin/python3
"""Module is a script that adds all arguments to a Python list,
and then save them to a file"""

from sys import argv

save_file = __import__('5-save_to_json_file').save_to_json_file
load_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    aList = load_file(filename)
except:
    aList = []
aList.extend(argv[1:])
save_file(aList, filename)
