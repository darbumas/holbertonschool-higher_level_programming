"""Unittest module for the function max_integer(list=[])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest class for max_integer()"""
    def test_integers(self):
        "test for valid input"
        self.assertEqual(max_integer([-2, 4, 2, -4]), 4)
        self.assertEqual(max_integer([2, 0]), 2)
        self.assertEqual(max_integer([-2, -1]), -1)
        self.assertEqual(max_integer([0, -4, -2]), 0)
        self.assertEqual(max_integer([-1, -2, -4]), -1)
        self.assertEqual(max_integer([11]), 11)

    def test_type(self):
        """test for data type"""
        self.assertEqual(max_integer([1, 2, 3, float('inf')]), float('inf'))
        self.assertEqual(max_integer("string"), 't')
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([1, 2, 3, float('nan')]), 3)

    def test_errors(self):
        """test exception"""
        self.assertRaises(TypeError, max_integer("max_integer"))
        self.assertRaises(TypeError, max_integer((2, 200)))
        self.assertRaises(TypeError, max_integer([1.2, 2.1, 3.2, 4.4]))

if __name__ == '__main__':
    unittest.mmain()
