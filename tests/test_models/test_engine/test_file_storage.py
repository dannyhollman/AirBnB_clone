#!/usr/bin/python3
""" Unit tests for File Storage """
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import unittest
import pep8


class test_file_storage(unittest.TestCase):
    """ class to test file storage """

    def test_pep8_conformance(self):
        """ conform to pep8 test """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/engine/file_storage.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
