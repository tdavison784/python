#!/usr/bin/python

class Employee():
    """Gathers employee info"""


    def __init__(self, first, last, salary='$5,000'):
        """Init all needed args for this class module"""
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, new_salary=''):
        """Give employee a raise
        this can also be a custom amount"""
        if new_salary == False:
            return self.salary
        else:
            return new_salary
