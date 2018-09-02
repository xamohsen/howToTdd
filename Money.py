

class Money:
    amount = 0
    currency = ""

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    @staticmethod
    def dollar(amount):
        return Money(amount, "USD")

    @staticmethod
    def franc(amount):
        return Money(amount, "CHF")

    def __eq__(self, money):
        return self.amount == money.amount and \
               self.currency == money.currency

    def getCurrency(self):
        return self.currency

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)
