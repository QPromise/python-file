import bank

acct = bank.account('Justin', '123-4567', 1000)
bank.deposit(acct, 500)
bank.withdraw(acct, 200)

# 顯示 Account(Justin, 123-4567, 1300)
print(bank.desc(acct))