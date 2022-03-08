#!/usr/bin/python3
"""A script that takes your GitHub credentials and displays your id"""
from sys import argv
import requests


if __name__ == "__main__":
    url = "https://api.github.com/user"
    cred = (argv[1], argv[2])
    resp = requests.get(url, auth=cred)
    obj = resp.json()
    print(obj.get('id'))
