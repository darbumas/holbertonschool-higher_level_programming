#!/usr/bin/python3
"""Unit test module for ``Rectangle`` class"""

import pep8
from models.rectangle import Rectangle
from models.base import Base
import unittest
from io import StringIO
import sys


class Test_Rectangle(unittest.TestCase):
    """class for testing the ``Rectangle`` class"""
    def test_classAttr_id(self):
        """test for setting id"""
        Base._Base__nb_objects = 0

        obj_1 = Rectangle(1, 9)
        self.assertEqual(obj_1.id, 1)
        obj_2 = Rectangle(1, 5, 2, 7, 9)
        self.assertEqual(obj_2.id, 9)
        obj_3 = Rectangle(1, 5, 2, 7)
        self.assertEqual(obj_3.id, 2)
        obj_4 = Rectangle(1, 5, 2, 7, -2.35)
        self.assertEqual(obj_4.id, -2.35)
        obj_5 = Rectangle(1, 4, 3, 2, "id")
        self.assertEqual(obj_5.id, "id")

    def test_attribute_types(self):
        """test for type error exceptions for getter/setter methods"""
        Base._Base__nb_objects = 0

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            obj = Rectangle("w", 1, 2, 4)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            obj = Rectangle(2, "h", 3, 4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            obj = Rectangle(2, 1, "x", 4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            obj = Rectangle(2, 1, 3, "y")

    def test_attributes_values(self):
        """test for value error exceptions for setter/getter methods"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            obj = Rectangle(0, 3, 1, 4)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            obj = Rectangle(-2, 3, 1, 4)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            obj = Rectangle(2, 0, 4, 1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            obj = Rectangle(2, -1, 4, 1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            obj = Rectangle(2, 1, -1, 4)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            obj = Rectangle(3, 2, 1, -3)

    def test_area(self):
        """test the method that returns the area of a rectangle instance"""

        instance_1 = Rectangle(3, 2)
        self.assertEqual(instance_1.area(), 6)
        instance_2 = Rectangle(15, 10)
        self.assertEqual(instance_2.area(), 150)

    def test_display(self):
        """test public method to display a rectangle instance with "#"."""

        instance_1 = Rectangle(3, 3, 1, 1)
        displayed = StringIO()
        sys.stdout = displayed
        instance_1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(displayed.getvalue(), "\n ###\n ###\n ###\n")

        instance_2 = Rectangle(2, 3)
        displayed_i = StringIO()
        sys.stdout = displayed_i
        instance_2.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(displayed_i.getvalue(), "##\n##\n##\n")

    def test_str_overide(self):
        """test the __str__ method"""
        Base._Base__nb_objects = 0

        instance_1 = Rectangle(3, 2, 4, 1)
        self.assertEqual(instance_1.__str__(), "[Rectangle] (1) 4/1 - 3/2")
        instance_2 = Rectangle(4, 2)
        self.assertEqual(instance_2.__str__(), "[Rectangle] (2) 0/0 - 4/2")
        instance_id = Rectangle(5, 2, 3, 1, 9)
        self.assertEqual(instance_id.__str__(), "[Rectangle] (9) 3/1 - 5/2")

    def test_update_args(self):
        """test public method that updates the class"""
        Base._Base__nb_objects = 0

        obj = Rectangle(87, 9, 3, 11, 5)
        self.assertEqual(obj.__str__(), "[Rectangle] (5) 3/11 - 87/9")
        obj.update(1)
        self.assertEqual(obj.__str__(), "[Rectangle] (1) 3/11 - 87/9")
        obj.update(5, 3)
        self.assertEqual(obj.__str__(), "[Rectangle] (5) 3/11 - 3/9")
        obj.update(12, 4, 5)
        self.assertEqual(obj.__str__(), "[Rectangle] (12) 3/11 - 4/5")
        obj.update(2, 4, 6, 8)
        self.assertEqual(obj.__str__(), "[Rectangle] (2) 8/11 - 4/6")
        obj.update(-1, 2, 3, 5, 5)
        self.assertEqual(obj.__str__(), "[Rectangle] (-1) 5/5 - 2/3")

    def test_update_kwargs(self):
        Base._Base__nb_objects = 0

        obj = Rectangle(87, 9, 3, 11, 5)
        self.assertEqual(obj.__str__(), "[Rectangle] (5) 3/11 - 87/9")
        obj.update(id=-99)
        self.assertEqual(obj.__str__(), "[Rectangle] (-99) 3/11 - 87/9")
        obj.update(width=55)
        self.assertEqual(obj.__str__(), "[Rectangle] (-99) 3/11 - 55/9")
        obj.update(y=0)
        self.assertEqual(obj.__str__(), "[Rectangle] (-99) 3/0 - 55/9")
        obj.update(height=15, x=7, id=9)
        self.assertEqual(obj.__str__(), "[Rectangle] (9) 7/0 - 55/15")


if __name__ == "__main__":
    unittest.main()
