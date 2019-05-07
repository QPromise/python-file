import bank

acct = bank.Account('Justin', '123-4567', 1000)

def withdraw(acct):
    try:
        acct.withdraw(2000)
    except bank.BankingException as ex:
        print(ex)
        print('你要進行借貸嗎？')
        # 其他借貸流程

withdraw(acct)


def deposit(acct):
    try:
        acct.deposit(-500)
    except ValueError as err:
        import logging, datetime
        logging.getLogger(__name__).log(
            logging.ERROR,
            'Logging: {time}, {number}, {message}'.format(
                time = datetime.datetime.now(),
                number = acct.number,
                message = err
            )
        )
        raise bank.BankingException('輸入金額為負的行為已記錄') from err

deposit(acct)
