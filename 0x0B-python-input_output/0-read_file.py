#!/usr/bin/python3
"""function reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """Prints the content to stdout"""
    with open(filename, encoding="utf-8") as fil:
        print(fil.read(), end="")
