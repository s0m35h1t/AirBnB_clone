#!/usr/bin/python3
"""
Define: User class unitests
"""
import unittest
from email import email
from models.user import User


class TestUserMethods(unittest.TestCase):

    def test_email_is_str(self):
        self.assertEqual(str, type(user().email))
