#!/usr/bin/python3
"""function that adds a new attribute to an obj. if possible"""


def add_attribute(obj, attr, value):
    """add atribute method"""
    if hasattr(obj, '__dict__') is True:
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
