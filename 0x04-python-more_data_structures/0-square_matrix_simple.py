#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    num = []
    for u in matrix:
        num.append([c**2 for c in u])
    return num
