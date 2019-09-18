#!/usr/bin/python3
def max_integer(my_list=[]):
    count = len(my_list)
    if count == 0:
        return (None)
    n = my_list[0]
    for i in range(count):
        if n <= my_list[i]:
            n = my_list[i]
        else:
            continue
    return (n)
