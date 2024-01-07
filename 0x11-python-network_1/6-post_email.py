#!/usr/bin/python3
"""takes in URL,
- sends request to URL and displays the value
"""
import sys
import urllib.request

if __name__ == "__main__":
    link = sys.argv[1]

    request = urllib.request.Request(link)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
