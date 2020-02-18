#!/usr/bin/python3
import unittest
from models.base_model import BaseModel


class testbase(unittest.TestCase):

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_id(self):
        b = BaseModel()
        b1 = BaseModel()
        self.assertNotEqual(b.id, b1.id)
