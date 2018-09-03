

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

    def reduce(self, to):
        rate = Bank().rate(self, to)
        return Money(self.amount/rate, to)


class Bank:
    rates = {}

    def addRate(self, fromm, to, rate):
        self.rates[Pair(fromm, to)] = rate

    def getRate(self, fromm, to):
        return self.rates[{fromm: to}]

    def reduce(self, sum, to):
        if type(sum) == Money:
            return sum
        return sum.reduce(to)

    def rate(self, fromm, to):
        return 2 if (fromm == "CHF") and (to == "USD") else 1


class Sum:

    aged = Money()
    addend = Money()

    def __init__(self, aged, addend):
        self.aged = aged
        self.addend = addend

    def reduce(self, to):
        amount = self.aged.amount + self.addend.amount
        return Money.dollar(amount, to)


class Pair:
    fromm, to = "", ""

    def __init__(self, fromm, to):
        self.fromm = fromm
        self.to = to

    def __eq__(self, other):
        return self.fromm == other.fromm and\
               self.to == other.to

    def __hash__(self):
        return 0
