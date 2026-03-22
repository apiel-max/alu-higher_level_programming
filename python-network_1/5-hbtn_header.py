#!/usr/bin/python3
"""This module sends a GET request and prints the X-Request-Id header value."""
import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
