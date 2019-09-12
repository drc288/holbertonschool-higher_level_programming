#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    data = 0
    argc = len(argv)
    if argc == 1:
        print(0)
    else:
        for i in range(1, argc):
            data = int(argv[i]) + data
            continue
        print("{:d}".format(data))
