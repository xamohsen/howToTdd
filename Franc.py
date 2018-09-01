from Money import *


class Franc(Money):

    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Franc(self.amount*multiplier)
