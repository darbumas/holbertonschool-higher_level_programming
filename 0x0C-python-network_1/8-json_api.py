#!/usr/bin/python3
"""A script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""
from sys import argv
import requests


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) > 1:
        inpt = {'q': argv[1]}
    else:
        inpt = {'q': ""}

    try
        resp = requests.post(url, inpt)
        obj = resp.json()
        if len(obj) > 0:
            print("[{}] {}".format(obj['id'], obj['name']))
        else:
            print("No result")
    except:
        print("Not a valid JSON")

