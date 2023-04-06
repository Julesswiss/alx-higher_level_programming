#!/usr/bin/env python3

"""
Python script that sends a GET request to a specified URL and prints the response body.
"""

import argparse
import requests


def main(url: str) -> None:
    """Sends a GET request to the specified URL and prints the response body."""
    response = requests.get(url)

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send a GET request to a URL and print the response body.")
    parser.add_argument("url", help="URL to send the request to.")
    args = parser.parse_args()

    main(args.url)
