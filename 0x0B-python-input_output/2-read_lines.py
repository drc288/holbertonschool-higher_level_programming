#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """ read_lines - read lines with nb_lines """
    with open(filename, encoding="utf-8") as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        else:
            for i in range(nb_lines):
                print(f.readline(), end="")
