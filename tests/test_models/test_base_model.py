#!/usr/bin/python3
""" This is a test for the base_model class"""

import unittest
from os import remove
import pep8
from models.base_model import BaseModel
import inspect
import models
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """" Test for the base model class """

    def setUp(self):
        """ Try delete the file.json file"""
        try:
            remove('file.json')
        except BaseException:
            pass

    def test_pep8(self):
        """ Test for the pep8 formating"""
        styles = pep8.StyleGuide(quiet=True)
        checks = styles.check_files(['models/base_model.py'])
        self.assertEqual(checks.total_errors, 0,
                         'pep8 fail: {}'.format(checks.total_errors))

    def test_create_an_instance_(self):
        """ Test creating an instance"""
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)

    def test_to_dict(self):
        """ Validate the type of return of method to_dict"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model.save()
        my_model_json = my_model.to_dict()

        self.assertTrue(type(my_model_json), "<class 'dict'>")

    def test_check_atributes(self):
        """ Validate the type of attributes """
        instance = BaseModel()
        self.assertTrue(type(instance.id), "<class 'str'>")
        self.assertTrue(type(instance.created_at),
                        "<class 'datetime.datetime'>")
        self.assertTrue(type(instance.updated_at),
                        "<class 'datetime.datetime'>")

    def test_output(self):
        """ Validate the string representation """
        ins = BaseModel()
        string = "[{}] ({}) {}".format(
            type(ins).__name__, ins.id, ins.__dict__)

        self.assertEqual(string, str(ins))
