

class Money:
    _amount = 0

    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, money):
        print(type(self), "  ==> ", type(money))
        return self.amount == money.amount and type(self) == type(money)