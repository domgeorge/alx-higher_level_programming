#!/usr/bin/python3
"""class Square defn"""


class Square:
    """square rep"""

    def __init__(self, size=0):
        """initialization"""
        self.size = size

    @property
    def size(self):
        """set size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return square area"""
        return self.__size * self.__size

    def __eq__(self, notslf):
        return self.area() == notslf.area()

    def __ne__(self, notslf):
        return self.area() != notslf.area()

    def __lt__(self, notslf):
        return self.area() < notslf.area()

    def __le__(self, notslf):
        return self.area() <= notslf.area()

    def __gt__(self, notslf):
        return self.area() > notslf.area()

    def __ge__(self, notslf):
        return self.area() >= notslf.area()
