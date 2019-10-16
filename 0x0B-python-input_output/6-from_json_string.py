#!/usr/bin/python3
import json


def from_json_string(my_str):
    """ from_json_string - from json a python """
    a = json.loads(my_str)
    return a
