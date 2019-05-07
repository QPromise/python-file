class Account:
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance

    def check_amount(self, amount):
        if amount <= 0:
            raise IllegalMoneyException('金額必須是正數', amount)

    def deposit(self, amount):
        self.check_amount(amount)

        self.balance += amount

    def withdraw(self, amount):
        self.check_amount(amount)

        if amount > self.balance:
           raise InsufficientException('餘額不足', self.balance)

        self.balance -= amount

    def __str__(self):
        return 'Account({name}, {number}, {balance})'.format(
            name = self.name, number = self.number, balance = self.balance
        )

class BankingException(Exception):
    def __init__(self, *args):
        super().__init__(args)

class IllegalMoneyException(BankingException):
    def __init__(self, message, money):
        super().__init__(message, money)
        self.money = money

    def __str__(self):
        return 'IllegalMoneyException: ' + super().__str__()

class InsufficientException(BankingException):
    def __init__(self, message, balance):
        super().__init__(message, balance)
        self.balance = balance

acct = Account('Justin', '123-4567', 1000)

def withdraw(acct):
    try:
        acct.withdraw(2000)
    except BankingException as ex:
        print(ex)
        print('你要進行借貸嗎？')
        # 其他借貸流程

withdraw(acct)


def deposit(acct):
    try:
        acct.deposit(-500)
    except IllegalMoneyException as err:
        import logging, datetime
        logging.getLogger(__name__).log(
            logging.ERROR,
            'Logging: {time}, {number}, {message}'.format(
                time = datetime.datetime.now(),
                number = acct.number,
                message = err
            )
        )
        raise BankingException('輸入金額為負的行為已記錄') from err

deposit(acct)

