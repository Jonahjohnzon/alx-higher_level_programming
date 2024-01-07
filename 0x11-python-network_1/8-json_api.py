#!/usr/bin/python3
"""A script that:
- takes in a search query letter as a command-line argument
- sends a POST request to http://0.0.0.0:5000/search_user
  with the search query letter as a parameter.
"""
import sys
import requests

if __name__ == "__main__":
    # Check if a search query letter is provided as a command-line argument
    search_query_letter = "" if len(sys.argv) == 1 else sys.argv[1]

    # Prepare the payload for the POST request
    payload = {"q": search_query_letter}

    # Send a POST request to the specified URL with the payload
    response = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        # Try to parse the response as JSON
        json_response = response.json()

        # Check if the response is an empty dictionary
        if json_response == {}:
            print("No result")
        else:
            # Print the result in the format: [id] name
            r = "[{}] {}".format(
                json_response.get("id"),
                json_response.get("name")
            )
            print(r)
    except ValueError:
        # Handle the case when the response is not a valid JSON
        print("Not a valid JSON")
