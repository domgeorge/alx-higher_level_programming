#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    rep = list(new.keys())
    for i in rep:
        new[i] *= 2
    return (new)
