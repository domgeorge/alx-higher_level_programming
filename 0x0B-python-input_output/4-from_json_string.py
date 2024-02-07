#!/usr/bin/python3
"""function returns an object (Python data structure)"""
import json


def from_json_string(my_str):
    """returns representation of a JSON string"""
    return json.loads(my_str)
