from Money import *


class Franc(Money):

    def __init__(self, amount):
        super().__init__(amount, "CHF")

    def times(self, multiplier):
        return Franc(self.amount*multiplier)

