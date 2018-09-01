class Franc:
    amount = 0

    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Franc(self.amount*multiplier)

    def __eq__(self, franc):
        return self.amount == franc.amount
