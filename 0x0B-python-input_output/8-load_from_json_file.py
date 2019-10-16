#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """ load_from_json_file - get the json and convert to python obj """
    with open(filename) as f:
        a = json.loads(f.read())
    return a