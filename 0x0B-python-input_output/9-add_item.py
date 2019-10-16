#!/usr/bin/python3
import json
import sys
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

new_list = []
filename = "add_item.json"
argc = len(sys.argv)

if argc <= 1:
    save_to_json_file(new_list, filename)
else:
    td = load_from_json_file(filename)
    for i in range(1, argc):
        td.append(sys.argv[i])
    save_to_json_file(td, filename)
    