#!/usr/bin/python3
""" Point number 1
"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as res:
        header = res.headers
        print(header.get("X-Request-Id"))
