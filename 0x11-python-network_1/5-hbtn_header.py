#!/usr/bin/env python3

"""
Python script that sends a request to the specified URL and prints the value of the "X-Request-Id" header in the response.
"""

import argparse
import requests


def main(url: str) -> None:
    """Sends a request to the specified URL and prints the value of the "X-Request-Id" header."""
    response = requests.get(url)

    print(response.headers.get("X-Request-Id"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send a request to a URL and print the value of the X-Request-Id header.")
    parser.add_argument("url", help="URL to send the request to.")
    args = parser.parse_args()

    main(args.url)
