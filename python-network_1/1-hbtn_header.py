#!/usr/bin/python3
"""Sends a GET request to a URL and displays the X-Request-Id header value."""
import urllib.request
import sys

request = urllib.request.Request(sys.argv[1])
with urllib.request.urlopen(request) as r:
    print(r.getheader('X-Request-Id'))
