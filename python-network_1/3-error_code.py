#!/usr/bin/python3
"""This module sends a request to a URL and handles HTTP error codes."""
import urllib.request
import urllib.error
import sys

try:
    with urllib.request.urlopen(sys.argv[1]) as r:
        print(r.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))
