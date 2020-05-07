#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    rslt = [[a ** 2 for a in row] for row in matrix]
    return rslt
