#!/usr/bin/python3
def write_file(filename="", text=""):
    """ write_file - write text ub filename """
    count = 0
    with open(filename, mode="w+", encoding="utf-8") as f:
        count = f.write(text)
    return count
