#!/usr/bin/python3
"""function that writes a str and return num of char"""


def write_file(filename="", text=""):
    """writes str to a UTF8 text file"""
    with open(filename, "w", encoding="utf-8") as fil:
        return fil.write(text)
