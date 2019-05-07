class Account:
    def __init__(self, name, number, balance):
        self.__name = name
        self.__number = number
        self.__balance = balance

    @property
    def name(self):
        return self.__name

    @property
    def number(self):
        return self.__number

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            print('存款金額不得為負')
        else:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print('餘額不足')
        else:
            self.__balance -= amount

    def __str__(self):
        return "Account('{name}', {number}, {balance})".format(
            name = self.__name, number = self.__number, balance = self.__balance
        )
