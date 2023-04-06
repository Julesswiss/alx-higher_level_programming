#!/usr/bin/env python3

"""
Python script that takes a URL as input, sends a request to the URL, and prints the response body
decoded in UTF-8. If the request raises an HTTPError, prints the error code.
"""

import argparse
import urllib.error
import urllib.request


def main(url: str) -> None:
    """Sends a request to the specified URL and prints the response body."""
    request = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send a request to a URL and print the response body.")
    parser.add_argument("url", help="URL to send the request to.")
    args = parser.parse_args()

    main(args.url)
