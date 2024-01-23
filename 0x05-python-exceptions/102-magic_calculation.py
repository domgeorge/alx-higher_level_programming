#!/usr/bin/python3
def magic_calculation(a, b):
    lister = 0
    for u in range(1, 3):
        try:
            if u > a:
                raise Exception('Too Far')
            lister += a ** b / u
        except Exception:
            lister = b + a
            break
    return lister
