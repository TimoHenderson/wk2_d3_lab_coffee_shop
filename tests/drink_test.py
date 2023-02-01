import unittest
from src.drink import Drink


class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Mocha", 5.00, 3)

    def test_has_name(self):
        self.assertEqual("Mocha", self.drink.name)

    def test_has_price(self):
        self.assertEqual(5.00, self.drink.price)

    def test_has_caffeine_level(self):
        self.assertEqual(3, self.drink.caffeine_level)
