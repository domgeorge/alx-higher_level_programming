#!/usr/bin/python3
"""function creates an Object"""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file"""
    with open(filename) as fil:
        return json.load(fil)
