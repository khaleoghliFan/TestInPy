import unittest
from unittest import TestCase

import test
class TestCal(TestCase):

    def test_add(self):
        c = test.Calculator(5, 2)
        result=c.add()
        self.assertEqual(7,result)
    def test_subtract(self):
        p=test.Calculator(6,12)
        result=p.subtract()
        self.assertEqual(-6,result)
    def test_divide(self):
        d=test.Calculator(12,6)
        result=d.divide()
        self.assertEqual(2,result)
    def test_multiply(self):
        d=test.Calculator(12,6)
        result=d.multiply()
        self.assertEqual(72,result)


if __name__=="__main()__":
    unittest.main()


if __name__ == '__main__':
    unittest.main()