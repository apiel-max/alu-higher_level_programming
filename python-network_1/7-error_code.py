#!/usr/bin/python3
"""This module sends a request and prints error code if HTTP status >= 400."""
import requests
import sys

r = requests.get(sys.argv[1])
if r.status_code >= 400:
    print("Error code: {}".format(r.status_code))
else:
    print(r.text)
