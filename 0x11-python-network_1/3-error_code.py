#!/usr/bin/python3
"""take in a URL,
- sends request to URL
- displays body ofresponse (decoded utf-8).
"""


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as resp:
            print(resp.read().decode('UTF-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
