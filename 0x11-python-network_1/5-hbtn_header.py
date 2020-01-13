#!/usr/bin/python3
import requests as req
import sys

if __name__ == "__main__":
    res = req.get(sys.argv[1])
    header = res.headers
    print(header.get("X-Request-Id"))
