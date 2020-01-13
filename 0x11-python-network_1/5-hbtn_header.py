#!/usr/bin/python3
import requests
import sys

res = requests.get(sys.argv[1])
print(res.headers.get("X-Request-Id"))
