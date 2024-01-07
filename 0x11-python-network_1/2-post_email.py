#!/usr/bin/python3
""" takes in a URL
- sends a POST request to URL
- takes email as parameter
- displays body of response
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    link = sys.argv[1]
    val = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(val).encode("ascii")

    request = urllib.request.Request(link, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
