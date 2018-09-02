from Money import *


class Dollar(Money):

    def __init__(self, amount):
        super().__init__(amount, "USD")
