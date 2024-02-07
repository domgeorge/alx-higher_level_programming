#!/usr/bin/python3
"""function appends a string"""


def append_write(filename="", text=""):
    """appends string to the end of a UTF8 text file"""
    with open(filename, "a", encoding="utf-8") as fil:
        return fil.write(text)
