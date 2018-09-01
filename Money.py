class Money:
    _amount = 0

    def __eq__(self, money):
        return self.amount == money.amount
