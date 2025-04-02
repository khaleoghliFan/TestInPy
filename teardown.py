import os
import unittest
from unittest import TestCase


class TestCal(TestCase):

    def setUp(self):
        """ایجاد یک فایل برای تست"""
        self.test_file = "test_file.txt"
        with open(self.test_file, "w") as f:
            f.write("This is a test file.")
    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
            print("remove")

    def test_file_contents(self):
        with open(self.test_file, "r") as f:
            contents = f.read()
        self.assertEqual(contents, "This is a test file.")
if __name__=="__main__":
    unittest.main()

