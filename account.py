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

    def withdraw(self, value):
        self.__balance -= value

    def transfer(self, value, destiny):
        self.withdraw(value)
        destiny.deposit(value)

    @property
    def balance(self):
        return self.__balance

    def get_holder(self):
        return self.__holder

    def get_number(self):
        return self.__number 

    @limit.setter
    def limit(self, limit):
        self.__limit = limit


    