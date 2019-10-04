#!/usr/bin/python3
"""
    matrix_divided - dividematrix with div
    >>> matrix_divided(matrix, 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    """
    matrix_divided - divide all elements of matrix with div
    """
    len_matrix = len(matrix)
    new_matrix = []
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        for item in matrix:
            for i in range(len(item)):
                if type(item[i]) is not int and type(item[i]) is not float:
                    raise TypeError("matrix must be a matrix (list of lists) \
                            of integers/floats")
            new_matrix.append(list(map(lambda x: round(x / div, 2), item)))
        if len_matrix != len(new_matrix):
            raise TypeError("Each row of the matrix must have the same size")
        return new_matrix
