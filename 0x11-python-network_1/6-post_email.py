#!/usr/bin/python3
import requests as req
import sys

payload = {'email': sys.argv[2]}
url = sys.argv[1]

res = req.post(url, data=payload)
print(res.text)
