#!/usr/bin/python3
"""
Define: City class unitests
"""
import unittest

from models.city import City
from datetime import datetime

class TestCityMethods(unittest.TestCase):

    def test_new_instance_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_datetime(self):
        self.assertEqual(datetime, type(City().created_at))


    def test_updated_at_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_no_args_instantiates(self):
        self.assertEqual(City, type(City()))
