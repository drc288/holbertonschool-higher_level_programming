#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tupla = ()
    a = len(tuple_a)
    b = len(tuple_b)
    if b == 0:
        tuple_b = (0,0)
    elif b < 2:
        tuple_b = tuple_b + (0,)

    if a == 0:
        tuple_a = (0,0)
    elif a < 2:
        tuple_a = tuple_a + (0,)

    tupla = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return (tupla)
