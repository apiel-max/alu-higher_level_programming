#!/usr/bin/python3
"""This module sends a POST request with email and prints the response."""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    values = urllib.parse.urlencode({'email': sys.argv[2]})
    data = values.encode('ascii')
    with urllib.request.urlopen(sys.argv[1], data) as r:
        print(r.read().decode('utf-8'))
