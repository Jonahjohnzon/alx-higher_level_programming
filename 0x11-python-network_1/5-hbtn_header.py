#!/usr/bin/python3
"""Display the X-Request-Id header variable of request to given URL
"""
import sys
import requests


if __name__ == "__main__":
    link = sys.argv[1]

    result = requests.get(link)
    print(result.headers.get("X-Request-Id"))
