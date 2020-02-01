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

    def test_reader_tuples(self):
        t = Py2Csv()
        t._read_file("resources/test_input_tuples.txt")
        self.assertEqual(t.output, [(1, 2), ('key', 'value'), ('timestamp', 'crime')])

    def test_reader_lists(self):
        t = Py2Csv()
        t._read_file("resources/test_input_lists.txt")
        self.assertEqual(t.output, [[1, 2], ['key', 'value'], ['timestamp', 'crime']])

    def test_tuple_writer_with_header(self):
        t = Py2Csv()
        t._read_file("resources/test_input_tuples.txt")
        t._write_file(self.output_file, header=['header1', 'header2'], mode='w+')
        with open(self.output_file) as f, open("resources/test_result_header.txt") as g:
            result = f.read()
            expected = g.read()
            self.assertEqual(result, expected)

    def test_list_write_with_header(self):
        t = Py2Csv()
        t._read_file("resources/test_input_lists.txt")
        t._write_file(self.output_file, header=['header1', 'header2'], mode='w+')
        with open(self.output_file) as f, open('resources/test_result_header.txt') as g:
            result = f.read()
            expected = g.read()
            self.assertEqual(result, expected)

    def test_convert_tuples(self):
        t = Py2Csv()
        t.convert('resources/test_input_tuples.txt', self.output_file)
        with open(self.output_file) as f, open("resources/test_result.txt") as g:
            result = f.read()
            expected = g.read()
            self.assertIsNotNone(result)
            self.assertEqual(result, expected)

    def test_convert_lists(self):
        t = Py2Csv()
        t.convert('resources/test_input_lists.txt', self.output_file)
        with open(self.output_file) as f, open("resources/test_result.txt") as g:
            result = f.read()
            expected = g.read()
            self.assertIsNotNone(result)
            self.assertEqual(result, expected)

    def test_convert_dicts(self):
        t = Py2Csv()
        t.convert('resources/test_input_dict.txt', self.output_file, fields=['date', 'crime', 'city'])
        with open(self.output_file) as f, open("resources/test_result_dict.txt") as g:
            result = f.read()
            expected = g.read()
            self.assertIsNotNone(result)
            self.assertEqual(result, expected)

    def test_convert_with_mode(self):
        t = Py2Csv()
        t.convert('resources/test_input_tuples.txt', self.output_file, header=['header1', 'header2'], mode='w+')
        t.convert('resources/test_input_tuples.txt', self.output_file, header=['header1', 'header2'], mode='a+')
        with open(self.output_file) as f, open("resources/test_result_appended.txt") as g:
            result = f.read()
            expected = g.read()
            self.assertIsNotNone(result)
            self.assertEqual(result, expected)

    def test_static_method_dict(self):
        Py2Csv.read_and_write_file('resources/test_input_dict.txt', self.output_file, fields=['date', 'crime', 'city'])
        with open(self.output_file) as f, open("resources/test_result_dict.txt") as g:
            result = f.read()
            expected = g.read()
            self.assertIsNotNone(result)
            self.assertEqual(result, expected)
