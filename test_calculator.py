import unittest
from unittest import TestCase

import test
class TestCal(TestCase):
    def setUp(self):
        self.c1=test.Calculator(6,12)
        self.c2=test.Calculator(-1,-1)
        self.c3=test.Calculator(-1,1)
    def tearDown(self): #run after test
        print("pass")
    def test_add(self):

        self.assertEqual(18, self.c1.add())
        self.assertEqual(-2, self.c2.add())
        self.assertEqual(0, self.c3.add())
    def test_subtract(self):

        self.assertEqual(-6,self.c1.subtract())
        self.assertEqual(0, self.c2.subtract())
        self.assertEqual(-2, self.c3.subtract())
    def test_divide(self):

        self.assertEqual(0.5, self.c1.divide())
        self.assertEqual(1, self.c2.divide())
        self.assertEqual(-1, self.c3.divide())
        #with ValueError
    def test_multiply(self):

        self.assertEqual(72, self.c1.multiply())
        self.assertEqual(1, self.c2.multiply())
        self.assertEqual(-1, self.c3.multiply())


if __name__=="__main__":
    unittest.main()
