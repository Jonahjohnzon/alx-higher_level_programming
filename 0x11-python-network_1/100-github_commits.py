#!/usr/bin/python3
"""List 10 most recent commits on a given GitHub repository.
"""
import sys
import requests

if __name__ == "__main__":
    # Extract repository owner and name from command-line arguments
    repo_owner = sys.argv[2]
    repo_name = sys.argv[1]

    # Create the GitHub API URL for the commits
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"

    # Send a GET request to the GitHub API
    response = requests.get(url)

    try:
        # Try to parse the response as JSON
        commits = response.json()

        # Iterate through the first 10 commits and print details
        for i in range(10):
            commit_sha = commits[i].get("sha")
            author_name = commits[i].get("commit").get("author").get("name")
            print(f"{commit_sha}: {author_name}")

    except IndexError:
        # Handle the case when there are fewer than 10 commits
        pass
