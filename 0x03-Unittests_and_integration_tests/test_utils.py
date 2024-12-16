#!/usr/bin/env python3
"""
In this task you will write the first unit test for utils.access_nested_map.

Create a TestAccessNestedMap class that inherits from unittest.TestCase.

Implement the TestAccessNestedMap.test_access_nested_map method to test that
the method returns what it is supposed to.

Decorate the method with @parameterized.expand to test the function for 
following inputs:

nested_map={"a": 1}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a", "b")
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test class as required above
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nestedmap, path, expected):
        """Test method as required above
        """
        self.assertEqual(access_nested_map(nestedmap, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nestedmap, path, message):
        """Uses the assertRaises context manager to test that a KeyError is
        raised and has correct message.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nestedmap, path)
            self.assertEqual(context.exception.args[0], message)
