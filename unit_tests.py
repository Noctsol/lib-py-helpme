"""
Owner: Kevin B
Contributors: N/A
Date Created: 20210818

Summary:
    This is tradition from all the people I've ever had the privilege of working with.
    Write lazy code. Why think when you can use helpu?

"""



# Local import
from helpu import helpu as hlp

import unittest
import os



class TestHelpu(unittest.TestCase):
    """ Unit tests """

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertTrue('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()


