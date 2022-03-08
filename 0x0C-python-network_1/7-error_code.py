#!/usr/bin/python3
"""A script that takes in a URL, sends a request to the URL
and displays the body of the response"""
from sys import argv
import requests


if __name__ == "__main__":
    resp = requests.get(argv[1])
    if resp.status_code <= 400:
        print(resp.text)
    else:
        print(f"Error code: {resp.status_code}")
