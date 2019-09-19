#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dir = sorted(a_dictionary.keys())
    for i in new_dir:
        print("{}: {}".format(i, a_dictionary[i]))
