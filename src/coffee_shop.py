class CoffeeShop:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def increase_till(self, amount):
        self.till += amount

    def sell_drink(self, drink, customer):
        if customer.age >= 16 and customer.energy_level <= 6:
            customer.spend_money(drink.price)
            self.increase_till(drink.price)
            self.reduce_stock_count(drink)
            customer.increase_energy_level(drink.caffeine_level)

    def reduce_stock_count(self, drink):
        for my_drink in self.drinks:
            if my_drink["drink"].name == drink.name:
                my_drink["stock"] -= 1
                return

    def sell_food(self, food, customer):
        customer.spend_money(food.price)
        self.increase_till(food.price)
        customer.decrease_energy_level(food.rejuvenation_level)

    def stock_value(self):
        stock_value = 0
        for drink in self.drinks:
            stock_value += drink["stock"] * drink["drink"].price
        return stock_value
