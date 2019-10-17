#!/usr/bin/python3
def number_of_lines(filename=""):
    """ number_of_lines - return the number of lines """
    with open(filename) as f:
        line = f.readlines()
    return len(line)
