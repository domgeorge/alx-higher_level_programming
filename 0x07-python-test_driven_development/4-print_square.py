#!/usr/bin/python3
"""function prints square with character #"""


def print_square(size):
    """size is the size length of the square / integer"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
