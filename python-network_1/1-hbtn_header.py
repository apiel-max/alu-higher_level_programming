#!/usr/bin/python3
"""This module sends a GET request to a URL and prints the X-Request-Id value."""
import urllib.request
import sys

request = urllib.request.Request(sys.argv[1])
with urllib.request.urlopen(request) as r:
    print(r.getheader('X-Request-Id'))
