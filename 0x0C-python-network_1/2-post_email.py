#!/usr/bin/python3
"""A script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the
body of the response"""
from sys import argv
import urllib.request
import urllib.error


if __name__ == "__main__":
    email = {'email': argv[2]}
    data = urllib.parse.urlencode(email)
    data = data.encode('utf-8')
    request = urllib.request.Request(argv[1], data)
    try:
        with urllib.request.urlopen(request) as res:
            response = res.read()
        print(response.decode('utf-8'))
    except urllib.error.URLError as e:
        print(e.reason)
