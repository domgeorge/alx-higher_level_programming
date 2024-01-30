#!/usr/bin/python3
"""Matrix multiplication"""


def matrix_mul(m_a, m_b):
    """function that multiplies 2 matrices"""
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(elem, int) or isinstance(elem, float))
               for elem in [numb for row in m_a for numb in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(elem, int) or isinstance(elem, float))
               for elem in [numb for row in m_b for numb in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    arr = []
    for i in range(len(m_b[0])):
        arr_row = []
        for j in range(len(m_b)):
            arr_row.append(m_b[j][i])
        arr.append(arr_row)

    arr1 = []
    for row in m_a:
        arr_row = []
        for arr_col in arr:
            prod = 0
            for i in range(len(arr[0])):
                prod += row[i] * arr_col[i]
            arr_row.append(prod)
        arr1.append(arr_row)

    return arr1
