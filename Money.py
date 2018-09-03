

class Money:
    amount = 0
    currency = ""

    def __init__(self, amount=0, currency=""):
        self.amount = amount
        self.currency = currency

    @staticmethod
    def dollar(amount, currency="USD"):
        return Money(amount, currency)

    @staticmethod
    def franc(amount, currency="CHF"):
        return Money(amount, currency)

    def __eq__(self, money):
        return self.amount == money.amount and \
               self.currency == money.currency

    def getCurrency(self):
        return self.currency

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)

    def plus(self, addend):
        return Sum(self, addend)


class Bank:

    def reduce(self, sum, to):
        if type(sum) == Money:
            return sum
        return sum.reduce(to)


class Sum:

    aged = Money()
    addend = Money()

    def __init__(self, aged, addend):
        self.aged = aged
        self.addend = addend

    def reduce(self, to):
        amount = self.aged.amount + self.addend.amount
        return Money.dollar(amount, to)
