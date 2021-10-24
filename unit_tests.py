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
import platform
import datetime

class TestHelpu(unittest.TestCase):
    """ Unit tests """

    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertTrue('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

    # Test file metadata functionality
    def test_file_metadata_funcs(self):
        """Test writing a csv, getting the file creation date,age, and deleting it"""

        # Dont run this test if this is windows
        if not platform.system() == "Windows":
            return True

        # Making pretend data to write to csv file in root
        csv_data = [["item","price"],["dog food", 100]]
        root = os.getcwd()
        file_path = os.path.join(root,"generic_test.csv")

        # Writing csv
        hlp.write_csv(file_path, csv_data)
        self.assertTrue(os.path.exists(file_path))                     # Asserts that the file exists

        # Getting file info
        creation_date = hlp.file_creation_date(file_path)
        self.assertTrue(isinstance(creation_date, datetime.datetime))  # Must be datetime

        creation_age = hlp.file_creation_age(file_path)
        self.assertTrue(isinstance(creation_age, float))               # Must be float

        # Delete File
        hlp.delete(file_path)
        self.assertFalse(os.path.exists(file_path))                    # File should no longer exists

if __name__ == '__main__':
    unittest.main()
