#!/usr/bin/python3
"""MyList inherits from list"""


class MyList(list):
    """contains class"""

    def print_sorted(self):
        """Print self sorted list"""
        print(sorted(self))
