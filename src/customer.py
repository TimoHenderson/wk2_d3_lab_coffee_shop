class Customer:
    def __init__(self, name, wallet, age, energy_level):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.energy_level = energy_level

    def spend_money(self, amount):
        self.wallet -= amount

    def increase_energy_level(self, amount):
        self.energy_level += amount

    def decrease_energy_level(self, amount):
        self.energy_level -= amount
        if self.energy_level < 0:
            self.energy_level = 0
