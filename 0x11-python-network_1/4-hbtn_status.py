#!/usr/bin/python3
"""Fetch https://intranet.hbtn.io/status."""
import requests

if __name__ == "__main__":
    try:
        result = requests.get("https://intranet.hbtn.io/status")
        result.raise_for_status()  # Check for HTTP errors

        print("Body response:")
        print("\t- type: {}".format(type(result.text)))
        print("\t- content: {}".format(result.text))
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

