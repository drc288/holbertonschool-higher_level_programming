#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("0 arguments.")
    argc = len(sys.argv) - 1
    for i in range(argc):
            if argc == 1:
                print("{:d} argument:".format(argc))
                print("{:d}: {}".format(argc, sys.argv[argc]))
                break
            else:
                print("{:d} arguments:".format(argc))
                for i in range(0, argc):
                    print("{:d}: {}".format(i + 1, sys.argv[i + 1]))
                    continue
                break
