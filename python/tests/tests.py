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

    def test_permutation_diff_size(self):
        self.assertFalse(str_1_2_permutation.permutation_of_str(
            self.test_strings["str_1_2_permutation_s1"],
            self.test_strings["str_1_2_permutation_s5"]
        ))
    
    def test_permutation_1(self):
        self.assertTrue(str_1_2_permutation.permutation_of_str(
            self.test_strings["str_1_2_permutation_s1"],
            self.test_strings["str_1_2_permutation_s2"]
        ))
    
    def test_permutation_2(self):
        self.assertFalse(str_1_2_permutation.permutation_of_str(
            self.test_strings["str_1_2_permutation_s1"],
            self.test_strings["str_1_2_permutation_s3"]
        ))
    
    def test_permutation_3(self):
        self.assertFalse(str_1_2_permutation.permutation_of_str(
            self.test_strings["str_1_2_permutation_s1"],
            self.test_strings["str_1_2_permutation_s4"]
        ))

    def test_permutation_4(self):
        self.assertFalse(str_1_2_permutation.permutation_of_str(
            self.test_strings["str_1_2_permutation_s5"],
            self.test_strings["str_1_2_permutation_s6"]
        ))



if __name__ == '__main__':
    unittest.main()