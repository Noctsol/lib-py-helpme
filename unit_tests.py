"""
Owner: Kevin B
Contributors: N/A
Date Created: 20210818

Summary:
    This is tradition from all the people I've ever had the privilege of working with.
    Write lazy code. Why think when you can use helpu?

"""



# Local import
from src import helpu as hlp

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

    def test_mkdir(self):
        """Make a directory and check if it exists and delete it"""
        root = os.getcwd()
        new_dir = os.path.join(root, "testmkdir/")
        print(new_dir)

        try:
            hlp.mkdir(new_dir)
            self.assertTrue(os.path.exists(new_dir))                     # Asserts that the file exists
        finally:
            hlp.delete(new_dir)

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

    def test_cut_paste_dir(self):
        """Test cut paste functionality on folder"""
        try:
            # Settings paths
            root = os.getcwd()
            src = os.path.join(root, "pointA")
            dst = os.path.join(root, "pointB")

            # Making directories
            hlp.mkdir(src)
            hlp.mkdir(dst)

            # Writing text files
            n_files = 5
            txt = "testing dah cut paste"
            txt_files_to_make = [os.path.join(src, f"{i}.txt") for i in range(n_files)]

            for file in txt_files_to_make:
                hlp.write_text(file, txt)

            # Cut paste
            hlp.cut_paste(src, dst)

            # Check
            concatbool = len(os.listdir(dst)) != 0 and len(os.listdir(dst)) == 1
            self.assertTrue(concatbool)

        finally:
            hlp.delete(src)
            hlp.delete(dst)

    def test_cut_paste_files(self):
        """Test cut paste functionality on folder"""
        try:
            # Settings paths
            root = os.getcwd()
            src = os.path.join(root, "pointA.txt")
            dst = os.path.join(root, "pointB.txt")

            txt = "testing dah cut paste"

            # Write src file
            hlp.write_text(src, txt)

            # Cut paste file
            hlp.cut_paste(src, dst)

            # Check
            concatbool = not os.path.exists(src) != 0 and os.path.exists(dst)
            self.assertTrue(concatbool)

        finally:
            hlp.delete(src)
            hlp.delete(dst)

    def test_copy_paste(self):
        """ Test copy paste functionality"""
        try:
            # Settings paths
            root = os.getcwd()
            src = os.path.join(root, "pointA.txt")
            dst = os.path.join(root, "pointB.txt")

            txt = "testing dah coopy paste"

            # Write src file
            hlp.write_text(src, txt)

            hlp.copy_paste(src, dst)

            # Check
            concatbool = os.path.exists(src) and os.path.exists(dst)
            self.assertTrue(concatbool)

        finally:
            hlp.delete(src)
            hlp.delete(dst)

    def test_to_listdict(self):
        """Test converting nested lists to a list of dictionaries"""
        # Pretend data
        lislis = [["a","b"],[1, 2],[3, 4]]

        # Convert
        lisdict = hlp.to_listdict(lislis)

        # Check
        is_valid = True
        for i in lisdict:
            if not isinstance(i, dict):
                is_valid = False
                break

        self.assertTrue(is_valid)

    def test_to_listlist(self):
        """Test converting list of dictionaries to nested lists"""
        # Pretend data
        lisdict = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]

        # Convert
        lislis = hlp.to_listlist(lisdict)

        # Check
        is_valid = True
        for i in lislis:
            if not isinstance(i, list):
                is_valid = False
                break

        if lislis[0] != ['a','b']:
            is_valid = False

        if lislis[1] != [1, 2]:
            is_valid = False

        self.assertTrue(is_valid)

if __name__ == '__main__':
    unittest.main()
