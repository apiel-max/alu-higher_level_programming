#!/usr/bin/python3
"""This module sends a GET request and prints the X-Request-Id header value."""
import urllib.request
import sys

if __name__ == "__main__":
    request = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(request) as r:
        print(r.getheader('X-Request-Id'))
