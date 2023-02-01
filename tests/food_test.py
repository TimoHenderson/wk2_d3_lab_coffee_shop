import unittest
from src.food import Food


class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food("Sandwich", 4.80, 2)

    def test_has_parameters(self):
        self.assertEqual("Sandwich", self.food.name)
        self.assertEqual(4.80, self.food.price)
        self.assertEqual(2, self.food.rejuvenation_level)
