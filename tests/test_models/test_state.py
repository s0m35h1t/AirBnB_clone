#!/usr/bin/python3
"""
Define: State class unitests
"""
import unittest
from datetime import datetime
from models.state import State


class TestStateMethods(unittest.TestCase):

    def test_no_args_instantiates(self):
        self.assertEqual(state, type(state()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(state(), models.storage.all().values())

    def test_id_is_str(self):
        self.assertEqual(str, type(state().id))

    def test_created_at_datetime(self):
        self.assertEqual(datetime, type(state().created_at))

    def test_updated_at_datetime(self):
        self.assertEqual(datetime, type(state().updated_at))
