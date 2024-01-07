#!/usr/bin/python3
"""take in URL
- send request to URL
- display body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    link = sys.argv[1]

    rs = requests.get(link)
    if rs.status_code >= 400:
        print("Error code: {}".format(rs.status_code))
    else:
        print(rs.text)
