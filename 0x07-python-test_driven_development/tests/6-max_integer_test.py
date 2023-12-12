#!/usr/bin/python3
"""unittests"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittests define"""

    def test_ordered_list(self):
        """Test ordered list of int"""
        order = [1, 2, 3, 4]
        self.assertEqual(max_integer(order), 4)

    def test_unordered_list(self):
        """Test unordered list of int"""
        unorder = [1, 3, 4, 2]
        self.assertEqual(max_integer(unorder), 4)

    def test_max_at_beginning(self):
        """Test list with a start max value."""
        max_at_start = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_start), 4)

    def test_empty(self):
        """Test empty list."""
        emp = []
        self.assertEqual(max_integer(emp), None)

    def test_one_element(self):
        """Test a list with a single element."""
        one_elem = [3]
        self.assertEqual(max_integer(one_elem), 7)

    def test_floats(self):
        """ list of floats."""
        f = [1.53, 6.33, -9.123, 18.4, 6.0]
        self.assertEqual(max_integer(f), 15.2)

    def test_ints_floats(self):
        """list of ints and floats."""
        int_float = [1.73, 13.5, -3, 17, 8]
        self.assertEqual(max_integer(int_float), 15.5)

    def test_string(self):
        """Test string"""
        stri = "Jojo"
        self.assertEqual(max_integer(stri), 'r')

    def test_list_strings(self):
        """Test list strings."""
        strs = ["jojo", "is", "so", "crazy"]
        self.assertEqual(max_integer(strs), "name")

    def test_emptystring(self):
        """Test emptystring."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
