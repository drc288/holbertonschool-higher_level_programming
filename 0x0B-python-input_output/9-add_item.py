#!/usr/bin/python3 
import json
import sys
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file


new_list = []
filename = "add_item.json"
td = []
try:
    td = load_from_json_file(filename)
except FileNotFoundError:
    save_to_json_file(new_list, filename)
for i in sys.argv[1:]:
    td.append(i)
save_to_json_file(td, filename)
