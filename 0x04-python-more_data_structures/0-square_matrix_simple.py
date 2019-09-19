#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = [[x ** 2 for x in matrix[i]]for i in range(0, len(matrix))]
    return new
