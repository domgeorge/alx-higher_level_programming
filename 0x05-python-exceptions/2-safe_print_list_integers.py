#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    lister = 0
    for u in range(x):
        try:
            print("{:d}".format(my_list[u]), end="")
            lister += 1
        except (ValueError, TypeError):
            continue
    print()
    return lister
