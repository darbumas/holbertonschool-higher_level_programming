#!/usr/bin/python3
"""A script that takes in a URL, sends a request to the URL and displays
the value of the variable X-Request-Id in the response header"""
from sys import argv
import requests


if __name__ == "__main__":
    resp = requests.get(argv[1])
    print(resp.headers.get('x-request-id'))
