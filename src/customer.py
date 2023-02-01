class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def spend_money(self, amount):
        self.wallet -= amount
