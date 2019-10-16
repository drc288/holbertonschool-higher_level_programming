#!/usr/bin/python3
def append_write(filename="", text=""):
    """ append_write - append text in the file """
    count = 0
    with open(filename, mode="a+", encoding="utf-8") as f:
        count = f.write(text)
    return count
