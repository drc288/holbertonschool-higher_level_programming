#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a
    b = tuple_b
    suma = 0
    suma2 = 0
    tupla=()
    if len(b) == 0:
        tupla = (a[0], a[1])
        return(tupla)
    elif len(b) < 2:
        b = b + (0,)
        suma = a[0] + b[0]
        tupla = (suma, a[1])
        return (tupla)
    tupla = (a[0] + b[0], a[1] + b[1])
    return (tupla)
