#!/usr/bin/env python3

"""
Python script that takes a URL as input, sends a request to the URL, and
prints the value of the X-Request-Id variable found in the response header.
"""

import argparse
import urllib.request


def main(url: str) -> None:
    """Sends a request to the specified URL and prints the X-Request-Id header value."""
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get X-Request-Id from URL header.")
    parser.add_argument("url", help="URL to request.")
    args = parser.parse_args()

    main(args.url)
