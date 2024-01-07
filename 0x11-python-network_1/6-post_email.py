#!/usr/bin/python3
"""
takes in a URL and an email address
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    payl = {'email': argv[2]}
    r = requests.post(argv[1], data=payl)
    print(r.text)
