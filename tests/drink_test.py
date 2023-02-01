import unittest
from src.drink import Drink


class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Mocha", 5.00)

    def test_has_name(self):
        self.assertEqual("Mocha", self.drink.name)

    def test_has_price(self):
        self.assertEqual(5.00, self.drink.price)
