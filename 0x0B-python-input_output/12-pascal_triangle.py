#!/usr/bin/python3
"""function that returns lists of integers representing the Pascal triangle"""


def pascal_triangle(n):
    """Pascal Triangle of size n"""
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        i = triangle[-1]
        ele = [1]
        for j in range(len(i) - 1):
            elem.append(i[j] + i[j + 1])
        ele.append(1)
        triangle.append(ele)
    return triangle
