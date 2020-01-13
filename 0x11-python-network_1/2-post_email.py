#!/usr/bin/python3
import urllib.request
import sys


if __name__ == "__main__":
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode("ascii")
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as res:
        body = res.read()
        print(body.decode("utf-8"))
