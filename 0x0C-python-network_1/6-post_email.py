#!/usr/bin/python3
"""A script that takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter"""
from sys import argv
import requests


if __name__ == "__main__":
    email = {'email': argv[2]}
    resp = requests.post(argv[1], email)
    print(resp.text)
