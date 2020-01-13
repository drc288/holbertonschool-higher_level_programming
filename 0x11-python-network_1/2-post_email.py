#!/usr/bin/python3
import urllib.parse
import urllib.request
from sys import argv

hbtn_url = argv[1]
value = {'email': argv[2]}

if __name__ == "__main__":
    data = urllib.parse.urlencode(value)
    data = data.encode("ascii")
    req = urllib.request.Request(hbtn_url, data)
    with urllib.request.urlopen(req) as res:
        body = res.read()
        print(body.decode("utf-8"))
