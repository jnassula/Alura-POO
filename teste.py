def create_account(number, holder, balance, limit):
    account = {"number": number, "holder": holder, "balance": balance, "limit": limit}
    return account

def account_statement(account, holder, balance):
    print("{}'s balance is {}.".format(holder, balance))

def deposit(account, value):
        balance += value

def withdraw(account, value):
        balance -= value