#!/usr/bin/python3
# print body or error
import urllib.request
import sys


if __name__ == "__main__":
    try:
        hbtn_url = sys.argv[1]
        with urllib.request.urlopen(hbtn_url) as res:
            body = res.read()
            print(body.decode("utf-8"))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
