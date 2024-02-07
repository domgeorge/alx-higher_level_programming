#!/usr/bin/python3
"""JSON serialization of an object"""


def class_to_json(obj):
    """function that returns the dictionary description"""
    return obj.__dict__
