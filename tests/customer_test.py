import unittest
from src.customer import Customer


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Fred", 56.00)

    def test_has_name(self):
        self.assertEqual("Fred", self.customer.name)

    def test_has_wallet(self):
        self.assertEqual(56.00, self.customer.wallet)
