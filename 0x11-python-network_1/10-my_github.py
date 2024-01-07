#!/usr/bin/python3
"""tak your GitHub credentials (username and password)
- uses GitHub API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    result = requests.get("https://api.github.com/user", auth=auth)
    print(result.json().get("id"))
