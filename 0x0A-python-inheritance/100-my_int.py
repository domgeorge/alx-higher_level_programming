#!/usr/bin/python3
"""Module that implements MyInt"""


class MyInt(int):
    """Class representing rebel integer that swaps `==` and `!=`"""
    def __eq__(self, other):
        """Inverts the equality check"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverts the inequality check"""
        return super().__eq__(other)
