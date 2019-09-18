#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    lent = len(my_list)
    for i in range(lent):
        data = my_list[i] % 2
        if data == 0:
            new_list[i] = True
        else:
            new_list[i] = False
    return (new_list)
