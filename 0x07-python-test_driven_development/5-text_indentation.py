#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """function prints text with 2 \n after each of these chars: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text) and text[i] == " ":
        i = i + 1

    while i < len(text):
        print(text[i], end="")
        if text[i] == "\n" or text[o] in ".?:":
            if text[i] in ".?:":
                print("\n")
            i = i + 1
            while i < len(text) and text[i] == " ":
                i = i + 1
            continue
        i = i + 1
