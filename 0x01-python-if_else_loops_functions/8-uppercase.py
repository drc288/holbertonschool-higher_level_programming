#!/usr/bin/python3
def uppercase(str):
    for chrter in str:
        lett = ord(chrter)
        if lett > 96 and lett < 124:
            lett = lett - 32
        print("{}".format(chr(lett)), end="")
    print()
