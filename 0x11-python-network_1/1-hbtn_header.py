#!/usr/bin/python3
import urllib.request
from sys import argv

hbtn_url = argv[1]

if __name__ == "__main__":
    with urllib.request.urlopen(hbtn_url) as res:
        print(res.headers["X-Request-Id"])
