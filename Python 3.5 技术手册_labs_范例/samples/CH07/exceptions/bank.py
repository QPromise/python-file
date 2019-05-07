class Account:
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance

    def check_amount(self, amount):
        if amount <= 0:
            raise ValueError('金額必須是正數:' + str(amount))

    def deposit(self, amount):
        self.check_amount(amount)

        self.balance += amount

    def withdraw(self, amount):
        self.check_amount(amount)

        if amount > self.balance:
           raise BankingException('餘額不足')

        self.balance -= amount

    def __str__(self):
        return "Account('{name}', '{number}', {balance})".format(
            name = self.name, number = self.number, balance = self.balance
        )

class BankingException(Exception):
    def __init__(self, message):
        super().__init__(message)

