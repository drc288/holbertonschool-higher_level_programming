#!/usr/bin/python3
def no_c(my_string):
    n = 0
    for i in my_string:
        if ord(i) == 99 or ord(i) == 67:
            my_string = my_string[0:n] + my_string[n+1:]
        n = n + 1
    return (my_string)
