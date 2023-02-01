class CoffeeShop:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def increase_till(self, amount):
        self.till += amount

    def sell_drink(self, drink, customer):
        if customer.age >= 16:
            customer.spend_money(drink.price)
            self.increase_till(drink.price)
