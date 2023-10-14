#!/usr/bin/python3
"""Defines unittests for models/amenity.py"""

import os
import unittest
from models.amenity import Amenity
from datetime import datetime
from models import storage


class TestAmenityAttributes(unittest.TestCase):
    def test_amenity_id_is_string(self):
        amenity = Amenity()
        self.assertTrue(type(amenity.id) == str)

    def test_amenity_created_at_is_datetime(self):
        amenity = Amenity()
        self.assertTrue(type(amenity.created_at) == datetime)

    def test_amenity_updated_at_is_datetime(self):
        amenity = Amenity()
        self.assertTrue(type(amenity.updated_at) == datetime)

    def test_amenity_name_exists(self):
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))

    def test_amenity_name_is_string(self):
        amenity = Amenity()
        self.assertTrue(type(amenity.name) == str)

class TestAmenityMethods(unittest.TestCase):
    def test_amenity_str_method(self):
        amenity = Amenity()
        string = str(amenity)
        self.assertTrue("[Amenity]" in string)
        self.assertTrue("id" in string)
        self.assertTrue("created_at" in string)
        self.assertTrue("updated_at" in string)

class TestAmenitySaveMethod(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.amenity = Amenity()
        cls.amenity.save()

    @classmethod
    def tearDownClass(cls):
        storage.delete(cls.amenity)

    def test_amenity_save(self):
        updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(updated_at, self.amenity.updated_at)

class TestAmenityToDictMethod(unittest.TestCase):
    def test_amenity_to_dict(self):
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertTrue(type(amenity_dict) == dict)
        self.assertEqual(amenity_dict['id'], amenity.id)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['created_at'], amenity.created_at.isoformat())
        self.assertEqual(amenity_dict['updated_at'], amenity.updated_at.isoformat())
        self.assertTrue('name' in amenity_dict)

if __name__ == '__main__':
    unittest.main()
