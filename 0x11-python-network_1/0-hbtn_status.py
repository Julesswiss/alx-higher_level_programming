#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status.
"""
import urllib.request

if __name__ == "__main__":
    try:
        with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
            html = response.read()

            print('Body response:')
            print(f'\t- type: {type(html)}')
            print(f'\t- content: {html}')
            print(f'\t- utf8 content: {html.decode("utf-8", "replace")}')
    except urllib.error.URLError as e:
        print(f"Error: {e.reason}")
