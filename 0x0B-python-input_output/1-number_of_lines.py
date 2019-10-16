#!/usr/bin/python3
def number_of_lines(filename=""):
    """ number_of_lines - return the number of lines """
    count = 0
    with open(filename) as f:
        for line in f:
            count += 1
    return count - 1
