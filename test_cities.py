#!/usr/bin/python
import unittest
from city_functions import get_state_info

class CitiesTestCase(unittest.TestCase):
    """Class to test the case of cities and country"""

    def test_city_state_name(self):

        city_info = get_state_info("Minneapolis", "Minnesota")
        self.assertEqual(city_info, "Minneapolis Minnesota")


    def test_city_state_population(self):
        """Does 'Minneapolis Minnesota - 300,000' work?"""
        city_info = get_state_info("Minneapolis", "Minnesota", "300,000")
        self.assertEqual(city_info, "Minneapolis Minnesota - 300,000")

unittest.main()