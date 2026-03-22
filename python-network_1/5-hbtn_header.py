#!/usr/bin/python3
"""This module sends a GET request to a URL and prints the X-Request-Id value."""
import requests
import sys

r = requests.get(sys.argv[1])
print(r.headers.get('X-Request-Id'))
