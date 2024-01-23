#!/usr/bin/python3
"""class square defn"""


class Square:
    """square rep"""
    def __init__(self, size=0):
        """ integer: square size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
