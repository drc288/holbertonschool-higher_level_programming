#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 0
    if matrix is None:
        print()
    row = len(matrix)
    for i in range(row):
        nodo = len(matrix[i])
        for j in range(nodo):
            if j == nodo - 1:
                print("{:d}".format(matrix[i][j]), end = "")
            else:
                print("{:d}".format(matrix[i][j]), end = " ")
        print()

