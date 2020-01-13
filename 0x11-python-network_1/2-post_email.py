#!/usr/bin/python3
import urllib.parse
import urllib.request
import sys

value = {'email': sys.argv[2]}

if __name__ == "__main__":
    data = urllib.parse.urlencode(value)
    data = data.encode("ascii")
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as res:
        body = res.read()
        print(body.decode("utf-8"))
