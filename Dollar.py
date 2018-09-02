from Money import *


class Dollar(Money):

    def __init__(self, amount):
        super().__init__(amount, "USD")

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)

