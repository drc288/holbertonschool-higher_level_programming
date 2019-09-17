#!/usr/bin/python3
def element_at(my_list, idx):
    i = len(my_list)
    index = 0
    if idx < 0:
        return (None)
    elif idx > 0 and idx < i:
        return (my_list[idx])
    return (None)
