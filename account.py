class Account:

    def __init__(self, number, holder, balance, limit):
        print("Building object ... {}".format(self))
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit

    def account_statement(self):
        print('The balance from {} is {}.'.format(self.__holder, self.__balance))

    def deposit(self, value):
        self.__balance += value

    def __can_witdraw(self, amount_to_withdraw):
        amount_available_to_withdraw = self.__balance + self.__limit
        return amount_to_withdraw <= amount_available_to_withdraw

    def withdraw(self, value):
        if(self.__can_witdraw(value)):
            self.__balance -= value
        else:
            print("{} value exceeded limit.".format(value))

    def transfer(self, value, destiny):
        self.withdraw(value)
        destiny.deposit(value)

    @property
    def balance(self):
        return self.__balance

    @property
    def holder(self):
        return self.__holder
    
    @property
    def number(self):
        return self.__number

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, limit):
        self.__limit = limit 


    