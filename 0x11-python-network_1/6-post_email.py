#!/usr/bin/python3
"""Takes in a URL,
sends a request to the URL and displays the value of the "X-Request-Id" header.
"""
import sys
import urllib.request

if __name__ == "__main__":
    # Assuming a URL is always provided as a command-line argument
    link = sys.argv[1]

    try:
        request = urllib.request.Request(link)
        with urllib.request.urlopen(request) as response:
            x_request_id = response.headers.get("X-Request-Id")

            if x_request_id is not None:
                print("X-Request-Id:", x_request_id)
            else:
                print("The 'X-Request-Id' header is not present in the response.")
    except urllib.error.URLError as e:
        print(f"Error: {e}")
