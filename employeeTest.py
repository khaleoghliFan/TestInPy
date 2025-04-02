import unittest
from unittest import TestCase
from unittest.mock import patch

import employee


class TestEmployee(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.emp1 = employee.Employee("ali", "khaleghi", 20)
        cls.emp2 = employee.Employee("hadi", "kama", 12)

    @classmethod
    def tearDownClass(cls):  # اصلاح نام تابع
        print("Teardown Class")

    def test_email(self):
        self.assertEqual(self.emp1.set_email, "ali.khaleghi@email.com")
        self.assertEqual(self.emp2.set_email, "hadi.kama@email.com")

    def test_url(self):
        with patch("employee.requests.get") as mocked_get:
            mocked_get.return_value.ok=True
            mocked_get.return_value.text = "success"
            response=self.emp1.monthly_schedule("may")
            mocked_get.assert_called_with(f"http://example.com/{self.emp1.family}/may")  # اصلاح متغیر
            self.assertEqual("success",response)
if __name__ == "__main__":
    unittest.main()
