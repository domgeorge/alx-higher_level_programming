#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    lists = list(a_dictionary.keys())
    lists.sort()
    for u in lists:
        print("{}: {}".format(u, a_dictionary.get(u)))
