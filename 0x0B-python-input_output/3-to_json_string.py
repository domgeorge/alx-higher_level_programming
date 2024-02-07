#!/usr/bin/python3
"""function returns the JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """string object returned"""
    return json.dumps(my_obj)
