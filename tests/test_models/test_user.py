#!/usr/bin/python3
"""Defines unittests for models/user.py.
"""
import models
import unittest
from datetime import datetime
from models.user import User


class TestUser_instantiation(unittest.TestCase):

    def test_no_args_instantiates(self):
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_str(self):
        self.assertEqual(str, type(User().id))

    def test_created_at_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_str(self):
        self.assertEqual(str, type(User.email))

    def test_password_is_str(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_str(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_str(self):
        self.assertEqual(str, type(User.last_name))

    def test_two_users_unique_ids(self):
        us1 = User()
        us2 = User()
        self.assertNotEqual(us1.id, us2.id)


if __name__ == "__main__":
    unittest.main()
