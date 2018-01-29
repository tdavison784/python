#!/usr/bin/python
import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Test for 'name_function.py'"""

    def test_first_last_name(self):
        """Do names like 'tommy davison' work?"""

        formatted_name = get_formatted_name("tommy", "davison")
        self.assertEqual(formatted_name, 'Tommy Davison')

    def test_first_last_middle_name(self):
        """Do names like 'tommy william davison' work?"""

        formatted_name = get_formatted_name("tommy", "davison", "william")
        self.assertEqual(formatted_name, "Tommy William Davison")

unittest.main()