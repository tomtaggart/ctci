#! /usr/bin/python3

import json
import unittest

import sys
sys.path.append('../')

from src import *


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        with open('test_data.json') as f:
            self.test_strings = json.load(f)

    def test_solution1_unique(self):
        self.assertFalse(str_1_1_dup_chars_sol1.dup_char_in_str(
            self.test_strings["str_1_1_unique_chars"]))

    def test_solution1_duplicate(self):
        self.assertTrue(str_1_1_dup_chars_sol1.dup_char_in_str(
            self.test_strings["str_1_1_duplicate_chars"]))

    def test_solution2_unique(self):
        self.assertFalse(str_1_1_dup_chars_sol2.dup_char_in_str(
            self.test_strings["str_1_1_unique_chars"]))

    def test_solution2_duplicate(self):
        self.assertTrue(str_1_1_dup_chars_sol2.dup_char_in_str(
            self.test_strings["str_1_1_duplicate_chars"]))

if __name__ == '__main__':
    unittest.main()