#!/usr/bin/python3
"""
 "2-matrix_divided" module.
"""


def matrix_divided(matrix, div):
    """
    divide matrix number by div
    Args:
        matrix : the first number
        div : the second number
    Returns:
        b
    """

    checkType = [int, float]
    lenm = len(matrix[0])
    if not type(div) in checkType:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        for j in i:
            if not type(j) in checkType:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(i) != lenm:
            raise TypeError("Each row of the matrix must have the same size")
    rslt = [[a / div for a in row] for row in matrix]
    b = [[round(a, 2) for a in row] for row in rslt]
    return b
