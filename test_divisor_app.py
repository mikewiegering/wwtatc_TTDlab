#! /usr/bin/env python

from divisors_app import *
import unittest
from unittest.mock import MagicMock, patch

class TestDivisorApp(unittest.TestCase):



    def setUp(self):
        self.divisors = Divisors()

    # Take unput from user- set_user_num
    def test_set_user_num(self):
        expected_num = 10
        with patch('builtins.input', side_effect=['10']):
            self.divisors.set_user_num()
        self.assertEqual(self.divisors.user_num, expected_num)

    # generate divisors and store in object
    def test_generate_divisors(self):
        control_number = 10
        expected_divisors = [1,2,5,10]
        with patch('builtins.input', side_effect=[control_number]):
            self.divisors.set_user_num()
            self.divisors.generate_divisors()
        self.assertEqual(self.divisors.divisors, expected_divisors)
