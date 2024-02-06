#!/usr/bin/python3
"""Module implementing funct to det class membership"""


def is_kind_of_class(obj, a_class):
    """Returns True if type(obj) is a_class or inherits from a_class"""
    return isinstance(obj, a_class)
