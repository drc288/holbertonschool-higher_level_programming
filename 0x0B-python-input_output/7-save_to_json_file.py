#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """ save_to_json_file - sabe a obj with python and convert in json """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
