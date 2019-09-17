#!/usr/bin/python3
def no_c(my_string):
    n = 0
    strn = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            strn = strn + i
    return (strn)
