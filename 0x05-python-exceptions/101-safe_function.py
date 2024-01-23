#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """execute a function safely"""
    try:
        lister = fct(*args)
        return lister
    except Exception as u:
        print("Exception: {}".format(u), file=sys.stderr)
        return None
