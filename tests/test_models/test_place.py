#!/usr/bin/python3
"""
Define: Place class unitests
"""
import unittest
import models
from datetime import datetime
from models.place import Place


class TestPlaceMethods(unittest.TestCase):

    def test_no_args_instantiates(self):
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_str(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))


if __name__ == "__main__":
    unittest.main()
