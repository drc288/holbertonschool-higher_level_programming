#!/usr/bin/python3
def search_replace(my_list, search, replace):
    f = lambda x: replace if x == search else x
    for i in range(0, len(my_list)):
        new = [f(x) for x in my_list]
    return new
