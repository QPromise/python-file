class Account:
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print('存款金額不得為負')
        else:
            self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print('餘額不足')
        else:
            self.balance -= amount

    def __str__(self):
        return "Account('{name}', '{number}', {balance})".format(
            name = self.name, number = self.number, balance = self.balance
        )
