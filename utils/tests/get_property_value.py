

from django.test import TestCase
from utils import get_first_item
from utils.get_property_value import get_property_value
from utils.print_context import _print_context
from utils.tests.setup import setup_test_data

class TestGetPropertyValue(TestCase):
    
    @classmethod
    def setUpTestData(cls):
       setup_test_data(cls)
        
    def test_01_primitives(self):
        _print_context(print_function_name=True)
        
        # If no prop is provided, return the item
        self.assertEqual(get_property_value(self.string), self.string)
        self.assertEqual(get_property_value(self.number), self.number)
        self.assertEqual(get_property_value(self.boolean), self.boolean)
        
        # If prop is provided, return None
        self.assertEqual(get_property_value(self.string, "length"), None)
        self.assertEqual(get_property_value(self.number, "value"), None)
        self.assertEqual(get_property_value(self.boolean, "value"), None)    
        
        # If custom default is provided, return the default
        self.assertEqual(get_property_value(self.string, "length", default="default"), "default")
        

    def test_02_dictionary_access(self):
        _print_context(print_function_name=True)
        
        # Basic property access
        self.assertEqual(get_property_value(self.dict_john, "name"), "John")
        
        # Nested property access
        self.assertEqual(get_property_value(self.dict_john, "address", "street"), "93 Main St")
        
        # Non-existent property
        self.assertEqual(get_property_value(self.dict_john, "nonexistent"), None)
        
        # Empty property name
        self.assertEqual(get_property_value(self.dict_john, ""), self.dict_john)
        self.assertEqual(get_property_value(self.dict_john, None), self.dict_john)
        
        # Custom default value
        self.assertEqual(get_property_value(self.dict_john, "nonexistent", default="default"), "default")


    def test_03_object_access(self):
        _print_context(print_function_name=True)
        
        # Basic attribute access
        self.assertEqual(get_property_value(self.object_jane, "name"), self.object_jane.name)
        
        # Nested attribute access
        self.assertEqual(get_property_value(self.object_jane, "address", "street"), self.object_jane.address['street'])

        # Non-existent attribute
        self.assertIsNone(get_property_value(self.object_jane, "nonexistent"))
        
        # Custome default value
        self.assertEqual(get_property_value(self.object_jane, "nonexistent", default="default"), "default")


        
        
        
        
        
        
        
        
    # ToDo: lists not yet implemented.
    # def test_05_tuple_access(self):
    #     print_object(print_function_name=True)
        
    #     test_tuple = ("first", "second", "third")
    #     self.assertEqual(get_property_value(test_tuple, 0), "first")
    #     self.assertEqual(get_property_value(test_tuple, "2"), "third")

    # ToDo: lists not yet implemented.
    # def test_06_list_access(self):
    #     print_object(print_function_name=True)
        
    #     # Integer index access
    #     self.assertEqual(get_property_value_simple(self.list_names, 0), self.list_names[0])
        
    #     # String index access
    #     self.assertEqual(get_property_value(self.list, "1"), "second")
        
    #     # Out of bounds index
    #     self.assertEqual(get_property_value(self.list, 10), None)
        
    #     # Invalid index
    #     self.assertEqual(get_property_value(self.list, "invalid"), None)
        
    #     # Custom default value
    #     self.assertEqual(get_property_value(self.list, "invalid", default="default"), "default")
        