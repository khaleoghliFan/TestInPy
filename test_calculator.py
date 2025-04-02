import unittest
from unittest import TestCase

import test
class TestCal(TestCase):

    def test_add(self):
        c = test.Calculator(5, 2)
        p = test.Calculator(-1, -1)
        q = test.Calculator(1, -1)
        self.assertEqual(7, c.add())
        self.assertEqual(-2, p.add())
        self.assertEqual(0, q.add())
    def test_subtract(self):
        p=test.Calculator(6,12)
        c = test.Calculator(-1, -1)
        q = test.Calculator(1, -1)
        self.assertEqual(-6,p.subtract())
        self.assertEqual(0, c.subtract())
        self.assertEqual(2, q.subtract())
    def test_divide(self):
        d=test.Calculator(12,6)
        c = test.Calculator(-1, -1)
        q = test.Calculator(1, -1)
        self.assertEqual(2, d.divide())
        self.assertEqual(1, c.divide())
        self.assertEqual(-1, q.divide())
    def test_multiply(self):
        d=test.Calculator(12,6)
        c = test.Calculator(-1, -1)
        q = test.Calculator(1, -1)
        self.assertEqual(72, d.multiply())
        self.assertEqual(1, c.multiply())
        self.assertEqual(-1, q.multiply())


if __name__=="__main()__":
    unittest.main()


if __name__ == '__main__':
    unittest.main()