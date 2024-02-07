#!/usr/bin/python3
"""function writes an Object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """writes object to a text file using JSON representation"""
    with open(filename, "w") as fil:
        json.dump(my_obj, fil)
