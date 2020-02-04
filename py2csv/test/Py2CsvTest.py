import os
import tempfile
import unittest

from src.Py2Csv import Py2Csv


class TestPy2Csv(unittest.TestCase):
    output_file = None

    @classmethod
    def setUp(self):
        self.output_file = tempfile.mktemp()

    @classmethod
    def tearDown(self):
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_convert_tuples(self):
        Py2Csv.convert('resources/test_input_tuples.txt', self.output_file)
        with open(self.output_file) as f, open("resources/test_result.txt") as g:
            result = f.read()
            expected = g.read()
            self.assertIsNotNone(result)
            self.assertEqual(result, expected)

    def test_convert_lists(self):
        Py2Csv.convert('resources/test_input_lists.txt', self.output_file)
        with open(self.output_file) as f, open("resources/test_result.txt") as g:
            result = f.read()
            expected = g.read()
            self.assertIsNotNone(result)
            self.assertEqual(result, expected)

    def test_convert_dicts(self):
        Py2Csv.convert('resources/test_input_dict.txt', self.output_file, fields=['date', 'crime', 'city'])
        with open(self.output_file) as f, open("resources/test_result_dict.txt") as g:
            result = f.read()
            expected = g.read()
            self.assertIsNotNone(result)
            self.assertEqual(result, expected)

    def test_convert_with_mode(self):
        Py2Csv.convert('resources/test_input_tuples.txt', self.output_file, header=['header1', 'header2'], mode='w+')
        Py2Csv.convert('resources/test_input_tuples.txt', self.output_file, header=['header1', 'header2'], mode='a+')
        with open(self.output_file) as f, open("resources/test_result_appended.txt") as g:
            result = f.read()
            expected = g.read()
            self.assertIsNotNone(result)
            self.assertEqual(result, expected)

    def test_convert_mixed_dict(self):
        Py2Csv.convert('resources/test_input_mixed.txt', self.output_file, fields=['date', 'crime', 'city'])
        with open(self.output_file) as f, open("resources/test_result_mixed.txt") as g:
            result = f.read()
            expected = g.read()
            self.assertIsNotNone(result)
            self.assertEqual(result, expected)
