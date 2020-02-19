#!/usr/bin/python3
"""
Define: BaseModel class unitests
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModelMethods(unittest.TestCase):

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_id(self):
        b = BaseModel()
        b1 = BaseModel()
        self.assertNotEqual(b.id, b1.id)

    def test_id_is_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))


if __name__ == "__main__":
    unittest.main()
