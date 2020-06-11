#! /usr/bin/env python

from divisors_app import *
import inittest
from unittest.mock import MagicMock, patch

class TestDivisorApp(unittest.TestCase):



    def setUp(self):
        self.divisors = divisors_app.Divosors()

    # Take unput from user- set_user_num
    def test_set_user_num(self):
        expected_num = 10
        with patch('builtins.input', side_effect=['10']):
            self.divisors.set_user_num()
        self.assertEqual(self.divisors.user_num, expected_num)


