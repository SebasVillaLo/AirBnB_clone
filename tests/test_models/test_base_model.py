#!/usr/bin/python3
"""
For base model
"""
import unittest
from models.base_model import BaseModel
base_model = __import__('base_model').__init__


class Testinit(unittest.TestCase):
    """
    Test base model
    """
