#!/usr/bin/python3
"""Unit test module for ``Base`` class"""

import unittest
from models.base import Base
from os import path

from models.rectangle import Rectangle
from models.square import Square


class Test_Base(unittest.TestCase):
    """class for testing the ``Base`` class."""
    def test_classAttr_id(self):
        """test if the private class attributes assigns the
        id as it should"""
        Base._Base__nb_objects = 0

        id_5 = Base(5)
        self.assertEqual(id_5.id, 5)

        id_0 = Base(0)
        self.assertEqual(id_0.id, 0)

        id_None = Base(None)
        self.assertEqual(id_None.id, 1)

        id_3 = Base()
        self.assertEqual(id_3.id, 2)

        id_6 = Base(6)
        self.assertEqual(id_6.id, 6)

        id_4 = Base()
        self.assertEqual(id_4.id, 3)

    def test_private_attr(self):
        """test to see if ``__nb_objects`` we can still access the
        private attribute"""
        new_obj = Base()
        self.assertTrue(hasattr(new_obj, "_Base__nb_objects"))

    def test_dumps_JSON(self):
        """test the static method that returns a JSON string"""

        reg_dict = {'id': 1, 'width': 3, 'height': 2, 'x': 4, 'y': 5}
        json_string = Base.to_json_string(reg_dict)
        self.assertTrue(isinstance(json_string, str))
        self.assertTrue(isinstance(reg_dict, dict))

        # case for empty dictionary
        empty_dict = {}
        json_string = Base.to_json_string(empty_dict)
        self.assertTrue(isinstance(empty_dict, dict))
        self.assertTrue(isinstance(json_string, str))

    def test_save_to_file(self):
        """test the class method that writes a json string to file"""

        new_obj = Rectangle(1, 3)
        next_obj = Rectangle(2, 4)
        Rectangle.save_to_file([new_obj, next_obj])
        self.assertEqual(path.exists("Rectangle.json"), True)

        new_obj = Square(1)
        next_obj = Square(4)
        Square.save_to_file([new_obj, next_obj])
        self.assertEqual(path.exists("Square.json"), True)

    def test_loads_JSON(self):
        """test the static method that returns a list of JSON string"""

        my_dict1 = {'id': 1, 'width': 3, 'height': 2, 'x': 4, 'y': 5}
        my_dict2 = {'id': 2, 'width': 2, 'height': 3, 'x': 5, 'y': 4}
        py_list = []
        py_list.append([my_dict1, my_dict2])

        # convert the list to json first
        json_string = Rectangle.to_json_string(py_list)

        # test the method from json
        from_json = Rectangle.from_json_string(json_string)
        self.assertEqual(py_list, from_json)

    def test_dict_to_instance(self):
        """test class method ``create()`` that returns an instance with
        all attributes already set"""
        Base._Base__nb_objects = 0

        dummy_rect = Rectangle(2, 9)
        my_rect = Rectangle.create(**dummy_rect.to_dictionary())
        self.assertEqual(dummy_rect.to_dictionary(), my_rect.to_dictionary())
        self.assertEqual(Base._Base__nb_objects, 2)

        dummy_square = Square(4)
        my_square = Square.create(**dummy_square.to_dictionary())
        self.assertEqual(dummy_square.to_dictionary(),
                         my_square.to_dictionary())
        self.assertEqual(Base._Base__nb_objects, 4)

    def test_file_to_instance(self):
        """test class method ``load_from_file(cls)`` that returns a list
        of instances."""
        Base._Base__nb_objects = 0

        obj_1 = Rectangle(4, 5)
        obj_2 = Rectangle(2, 3)
        obj_1_dict = obj_1.to_dictionary()
        obj_2_dict = obj_2.to_dictionary()
        list_obj = [obj_1, obj_2]
        Rectangle.save_to_file(list_obj)
        list_instances = Rectangle.load_from_file()

        self.assertIsInstance(list_instances[0], Rectangle)
        self.assertIsInstance(list_instances[1], Rectangle)

        self.assertDictEqual(list_instances[0].to_dictionary(), obj_1_dict)
        self.assertDictEqual(list_instances[1].to_dictionary(), obj_2_dict)

if __name__ == "__main__":
    unittest.main()
