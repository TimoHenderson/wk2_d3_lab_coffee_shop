import unittest
from src.drink import Drink


class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Mocha", 5.00)

    def test_has_name(self):
        self.assertEqual("Mocha", self.drink.name)
