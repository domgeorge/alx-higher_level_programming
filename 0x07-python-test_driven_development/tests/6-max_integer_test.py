#!/usr/bin/python3
"""maximum integer unittests"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define maximum integer unittests"""

    def test_ordered_list(self):
        """ordered list test"""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """unordered list test"""
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_begginning(self):
        """maximum value list test"""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """empty list test"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """single elem list test"""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_floats(self):
        """floats list tset"""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_and_floats(self):
        """ints and floats list test"""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
        """str test"""
        string = "David"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """strings list test"""
        strings = ["David", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """empty string test"""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
