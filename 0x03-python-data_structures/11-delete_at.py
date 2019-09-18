#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if not my_list:
        return None
    lent = len(my_list)
    if idx < 0:
        return my_list
    elif idx >= lent:
        return my_list
    my_list.remove(idx)
    return my_list