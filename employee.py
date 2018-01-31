#!/usr/bin/python

class Employee():
    """Gathers employee info"""


    def __init__(self, fullname, salary='$5,000'):
        """Init all needed args for this class module"""
        self.fullname = fullname
        self.salary = salary


    def give_raise(self, new_salary=''):
        """Give employee a raise
        this can also be a custom amount"""
        if new_salary:
            print(new_salary)
        else:
            print(self.salary)