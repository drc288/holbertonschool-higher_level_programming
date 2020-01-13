#!/usr/bin/python3
import requests

res = requests.get('https://intranet.hbtn.io/status')
print("Body response:")
print("\t- type: {}".format(type(res.text)))
print("\t- content: {}".format(res.text))
