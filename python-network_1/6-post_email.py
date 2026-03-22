#!/usr/bin/python3
"""This module sends a POST request with email parameter and prints response."""
import requests
import sys

if __name__ == "__main__":
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
