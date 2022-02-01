#!/usr/bin/python3
"""Unit test module for ``Square`` class."""

import unittest
from models.square import Square
from models.base import Base


class Test_Square(unittest.TestCase):
    """class for testing the ``Square`` class."""
    def test_classAttr_id(self):
        """test for setting id"""
        Base._Base__nb_objects = 0

        obj_1 = Square(1)
        self.assertEqual(obj_1.id, 1)
        obj_2 = Square(1, 5, 2, 7)
        self.assertEqual(obj_2.id, 7)
        obj_3 = Square(2)
        self.assertEqual(obj_3.id, 2)
        obj_4 = Square(5, 2, 7, -2.35)
        self.assertEqual(obj_4.id, -2.35)
        obj_5 = Square(4, 3, 2, "id")
        self.assertEqual(obj_5.id, "id")

    def test_attribute_types(self):
        """test for type error exceptions for getter/setter methods"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            obj = Square("w", 1, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            obj = Square(2, "x", 3, 2)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            obj = Square(2, 1, "y", 3)

    def test_area(self):
        """test public method area inherited from ``Rectangle``"""

        square1 = Square(1)
        self.assertEqual(square1.area(), 1)
        square2 = Square(2)
        self.assertEqual(square2.area(), 4)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            obj = Square(0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            obj = Square(-2)

    def test_str_overide(self):
        """test the __str__ method"""

        square1 = Square(5, 10, 10, 1)
        self.assertEqual(str(square1), "[Square] (1) 10/10 - 5")
        square2 = Square(2, 0, 0, 14)
        self.assertEqual(square2.__str__(), "[Square] (14) 0/0 - 2")

    def test_update_args(self):
        """test public method that updates the class with *args"""
        Base._Base__nb_objects = 0

        square = Square(5, 10, 10, 1)
        self.assertEqual(str(square), "[Square] (1) 10/10 - 5")
        square.update(20)
        self.assertEqual(str(square), "[Square] (20) 10/10 - 5")
        square.update(1, 4, 2, 3)
        self.assertEqual(str(square), "[Square] (1) 2/3 - 4")

    def test_update_kwargs(self):
        """test public method that updates the class with **kwargs"""
        Base._Base__nb_objects = 0

        square = Square(5, 10, 10, 1)
        self.assertEqual(str(square), "[Square] (1) 10/10 - 5")
        square.update(id=3)
        self.assertEqual(str(square), "[Square] (3) 10/10 - 5")
        square.update(size=23)
        self.assertEqual(str(square), "[Square] (3) 10/10 - 23")
        square.update(x=0, y=0)
        self.assertEqual(str(square), "[Square] (3) 0/0 - 23")

    def test_to_dict(self):
        """test the public method to_dictionary"""
        Base._Base__nb_objects = 0

        square = Square(5, 10, 10, 1)
        my_dict = square.to_dictionary()
        self.assertEqual(my_dict, {'id': 1, 'x': 10, 'y': 10, 'size': 5})

if __name__ == "__main__":
    unittest.main()
