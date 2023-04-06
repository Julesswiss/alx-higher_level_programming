#!/usr/bin/env python3

"""
Python script that takes a URL and an email address as input, sends a POST request to the URL with
the email as a parameter, and prints the response body decoded in UTF-8.
"""

import argparse
import urllib.parse
import urllib.request


def main(url: str, email: str) -> None:
    """Sends a POST request to the specified URL with the email as a parameter and prints the response body."""
    data = urllib.parse.urlencode({"email": email}).encode("ascii")
    request = urllib.request.Request(url, data=data, method="POST")

    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send a POST request to a URL with an email parameter.")
    parser.add_argument("url", help="URL to send the request to.")
    parser.add_argument("email", help="Email address to send as a parameter in the POST request.")
    args = parser.parse_args()

    main(args.url, args.email)
