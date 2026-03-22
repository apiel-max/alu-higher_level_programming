#!/usr/bin/python3
"""Sends a POST request with email parameter and displays the response."""
import requests
import sys

r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
print(r.text)
