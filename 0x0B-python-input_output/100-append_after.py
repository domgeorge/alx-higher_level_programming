#!/usr/bin/python3
"""function that inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """inserts text after each line containing a given str in a file"""
    txt = ""
    with open(filename) as i:
        for ln in i:
            txt += ln
            if search_string in ln:
                txt += new_string
    with open(filename, "w") as j:
        j.write(txt)
