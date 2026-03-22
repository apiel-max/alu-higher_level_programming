#!/usr/bin/python3
"""This module sends a POST request with a letter and displays search result."""
import requests
import sys

q = sys.argv[1] if len(sys.argv) > 1 else ""
r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
try:
    data = r.json()
    if data:
        print("[{}] {}".format(data.get('id'), data.get('name')))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
