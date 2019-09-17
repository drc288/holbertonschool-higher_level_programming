#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    l1 = my_list.copy()
    if idx < 0:
        return (l1)
    if idx >= len(my_list):
        return (l1)
    l1[idx] = element
    return (l1)
