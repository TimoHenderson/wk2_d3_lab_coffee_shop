import unittest
from src.coffee_shop import CoffeeShop
from src.drink import Drink
from src.customer import Customer


class TestCoffeeShop(unittest.TestCase):
    def setUp(self):
        self.drinks = [
            Drink("Mocha", 5.00),
            Drink("Latte", 4.50),
            Drink("Hot Chocolate", 3.60),
            Drink("Tea", 2.00),
        ]
        self.customer = Customer("Fred", 56.00)
        self.coffee_shop = CoffeeShop("The Prancing Pony", 100.00, self.drinks)

    def test_has_name(self):
        self.assertEqual("The Prancing Pony", self.coffee_shop.name)

    def test_has_till(self):
        self.assertEqual(100.00, self.coffee_shop.till)

    def test_increase_till(self):
        self.coffee_shop.increase_till(10.00)
        self.assertEqual(110.00, self.coffee_shop.till)

    def test_has_drinks(self):
        self.assertEqual(self.drinks, self.coffee_shop.drinks)

    def test_sell_drink(self):
        drink = self.drinks[1]
        self.coffee_shop.sell_drink(drink, self.customer)
        self.assertEqual(104.50, self.coffee_shop.till)
        self.assertEqual(51.50, self.customer.wallet)
