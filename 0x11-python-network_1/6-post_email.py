#!/usr/bin/env python3

"""
Python script that sends a POST request to a specified URL with an email parameter,
and prints the response body.
"""

import argparse
import requests


def main(url: str, email: str) -> None:
    """Sends a POST request to the specified URL with the email parameter, and prints the response body."""
    data = {"email": email}
    response = requests.post(url, data=data)

    print(response.text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send a POST request to a URL with an email parameter.")
    parser.add_argument("url", help="URL to send the request to.")
    parser.add_argument("email", help="Email parameter to include in the request.")
    args = parser.parse_args()

    main(args.url, args.email)
