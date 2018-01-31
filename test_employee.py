#!/usr/bin/python
import unittest
from employee import Employee

class TestEmployeeClass(unittest.TestCase):
    """Class to run a unit test on the employee module
    Makes sure that the module can accept a defualt salary
    as well as a optional new salary
    """

    def setUp(self):
        """Setup all needed args to use later in class"""
        fullname = "Tommy Davison"
        self.my_employee = Employee(fullname)

    def test_default_salary(self):
        """Does default salary work?"""

        self.assertIn(self.my_employee.give_raise(), self.my_employee.give_raise())

    def test_custom_salary(self):
        """Does $10,000 work?"""
        self.assertIn(self.my_employee.give_raise('$10,000'), self.my_employee.give_raise('$10,000'))

unittest.main()