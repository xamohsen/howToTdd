

class Money:
    amount = 0
    _currency = ""

    def __init__(self, amount, currency):
        self.amount = amount
        self._currency = currency

    def __eq__(self, money):
        return self.amount == money.amount and type(self) == type(money)

    def currency(self):
        return self._currency
