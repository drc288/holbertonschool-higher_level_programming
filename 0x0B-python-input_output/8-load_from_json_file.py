#!/usr/bin/python3
""" Load a json from file """
import json


def load_from_json_file(filename):
    """ load_from_json_file - get the json and convert to python obj """
    with open(filename, encoding="utf-8") as f:
        a = json.loads(f.read())
    return a
