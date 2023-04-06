#!/usr/bin/python3

"""
Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id.
"""

import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]

    response = requests.get(url, auth=(username, password))

    if response.status_code == 401:
        print("Incorrect credentials")
    elif response.status_code == 403:
        print("Access denied")
    else:
        try:
            data = response.json()
            print(data["id"])
        except ValueError:
            print("No valid JSON data found")
