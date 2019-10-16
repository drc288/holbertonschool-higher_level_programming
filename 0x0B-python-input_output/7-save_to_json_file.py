#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """ save_to_json_file - sabe a obj with python and convert in json """
    data_JSON = json.dumps(my_obj)
    with open(filename, mode="w") as f:
        f.write(data_JSON)
