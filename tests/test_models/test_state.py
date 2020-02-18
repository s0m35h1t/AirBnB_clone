#!/usr/bin/python3
"""
Define: State class unitests
"""
import unittest
import models
from datetime import datetime
from models.state import State


class TestStateMethods(unittest.TestCase):

    def test_no_args_instantiates(self):
        self.assertEqual(State, type(State()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(State(), models.storage.all().values())

    def test_id_is_str(self):
        self.assertEqual(str, type(State().id))

    def test_created_at_datetime(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at_datetime(self):
        self.assertEqual(datetime, type(State().updated_at))
