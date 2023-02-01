import unittest
from src.customer import Customer


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Fred", 56.00, 57, 1)

    def test_has_name(self):
        self.assertEqual("Fred", self.customer.name)

    def test_has_wallet(self):
        self.assertEqual(56.00, self.customer.wallet)

    def test_spend_money(self):
        self.customer.spend_money(5.00)
        self.assertEqual(51.00, self.customer.wallet)

    def test_has_age(self):
        self.assertEqual(57, self.customer.age)

    def test_has_energy_level(self):
        self.assertEqual(1, self.customer.energy_level)
