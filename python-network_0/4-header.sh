#!/bin/bash
# Sends a GET request to a URL with header X-HolbertonSchool-User-Id value 98
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
