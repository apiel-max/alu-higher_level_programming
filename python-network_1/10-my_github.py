#!/usr/bin/python3
"""Uses GitHub API to display user id using Basic Authentication."""
import requests
import sys

r = requests.get('https://api.github.com/user',
                 auth=(sys.argv[1], sys.argv[2]))
print(r.json().get('id'))
