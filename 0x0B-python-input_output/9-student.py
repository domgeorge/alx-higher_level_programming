#!/usr/bin/python3
"""class definition of Object"""


class Student:
    """student representation"""

    def __init__(self, first_name, last_name, age):
        """Initializing a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dictionary representation"""
        return self.__dict__
