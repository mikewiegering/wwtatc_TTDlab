#! /usr/bin/env python

class Divisors:
    
    def _init_(self):
        self.user_num = 0
        self.divisors = []

    def set_user_num(self):
        self.user_num = int(input("Enter a natural number: "))

    # def generate_divisors(self):