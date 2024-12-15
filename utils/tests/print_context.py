"""
python manage.py test utils.tests.print_object.TestPrintObject.test_01_basic_property
python manage.py test utils.tests.print_object.TestPrintObject.test_01_basic_property
python manage.py test utils.tests.print_object.TestPrintObjectDecorator
"""
# from django.test import TestCase
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from utils.print_context import _print_context, print_context_decorator


class TestSimpleObject:
    def __init__(self):
        self.name = "Test"
        self.value = 42
    def __str__(self):
        return "TestObject"

class TestPrintObject(TestCase):
    def setUp(self):
        self.test_obj = TestSimpleObject()
        self.output = StringIO()
        self.patcher = patch('sys.stdout', self.output)
        self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_01_basic_property(self):
        _print_context(self.test_obj, "name")
        expected = "    - TestSimpleObject = TestObject\n      - name: Test\n"
        self.assertEqual(self.output.getvalue(), expected)

    def test_02_multiple_properties(self):
        _print_context(self.test_obj, "name", "value")
        expected = "    - TestSimpleObject = TestObject\n      - name: Test, value: 42\n"
        self.assertEqual(self.output.getvalue(), expected)

    def test_03_literal_string(self):
        _print_context(self.test_obj, "-Hello")
        expected = "    - TestSimpleObject = TestObject\n      - Hello\n"
        self.assertEqual(self.output.getvalue(), expected)

    def test_04_missing_property(self):
        _print_context(self.test_obj, "missing_prop")
        expected = "    - TestSimpleObject = TestObject\n      - missing_prop: not found\n"
        self.assertEqual(self.output.getvalue(), expected)

    def test_05_mixed_content(self):
        _print_context(self.test_obj, "name", "-> ", "value")
        expected = "    - TestSimpleObject = TestObject\n      - name: Test\n      - > value: 42\n"
        self.assertEqual(self.output.getvalue(), expected)

    def test_06_no_properties(self):
        _print_context(self.test_obj)
        expected = "    - TestSimpleObject = TestObject\n"
        self.assertEqual(self.output.getvalue(), expected)

    def test_07_none_object(self):
        _print_context(None)
        expected = "    - NoneType = None\n"
        self.assertEqual(self.output.getvalue(), expected)

@print_context_decorator
class TestPrintObjectDecorator(TestCase):
    def test_01_my_test(self):
        self.assertEqual(1, 1)

    def test_02_my_test(self):
        self.assertEqual(2, 2)
