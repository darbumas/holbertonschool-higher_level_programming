#!/usr/bin/python3
"""A script that fetcheds 'https://intranet.hbtn.io/status'"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as res:
        response = res.read()
    print('Body Response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}'
           .format(type(response), response, response.decode('utf-8')))
