#!/usr/bin/python3
import requests as req
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    res = req.get(url)
    code = res.status_code
    if code <= 400:
        print(res.text)
    else:
        print("Error code: {}".format(code))
