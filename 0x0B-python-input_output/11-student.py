#!/usr/bin/python3
"""class Student that defines student"""


class Student:
    """student representation"""

    def __init__(self, first_name, last_name, age):
        """Initializing student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionary representation"""
        if (type(attrs) == list and
                all(type(elem) == str for elem in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__

    def reload_from_json(self, json):
        """replace student attributes"""
        for j, k in json.items():
            setattr(self, j, k)
