#!/usr/bin/python3
"""A script that takes in a URL, sends a request to the URL and
displays the body of the response"""
from sys import argv
import urllib.request


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as res:
            response = res.read()
        print(response.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
    except urllib.error.URLError as e:
        print(f"Error code: {e.reason}")
