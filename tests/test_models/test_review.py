#!/usr/bin/python3
"""
Define: Review class unitests
"""
import unittest
import models
from datetime import datetime
from models.review import Review


class TestReviewMethods(unittest.TestCase):

    def test_no_args_instantiates(self):
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_id_is_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))


if __name__ == "__main__":
    unittest.main()
