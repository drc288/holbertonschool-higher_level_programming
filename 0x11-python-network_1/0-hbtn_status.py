#!/usr/bin/python3
import urllib.request

hbtn_url = "https://intranet.hbtn.io/status"

if __name__ == "__main__":
    with urllib.request.urlopen(hbtn_url) as res:
        body = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
