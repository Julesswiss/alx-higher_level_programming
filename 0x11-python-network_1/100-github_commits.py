#!/usr/bin/python3

"""
Python script that takes 2 arguments to retrieve the 10 most recent
commits from a given repository on GitHub, and displays the SHA
and the author of each commit.
"""

import sys
import requests


if __name__ == "__main__":
    # Check if enough arguments were provided
    if len(sys.argv) < 3:
        print("Usage: {} <owner> <repo>".format(sys.argv[0]))
        sys.exit(1)

    # Build URL for GitHub API
    owner = sys.argv[1]
    repo = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    # Send request to GitHub API
    try:
        response = requests.get(url)
        response.raise_for_status()
        commits = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Display the SHA and the author of each commit
    for commit in commits[:10]:
        sha = commit["sha"]
        author = commit["commit"]["author"]["name"]
        print(f"{sha}: {author}")
