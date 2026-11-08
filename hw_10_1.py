class BankAccount:
    def __init__(self, owner, _balance, accaunt_number):
        self._owner = owner
        self._balance = _balance
        self._accaunt_number = accaunt_number

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        elif amount <= 0:
            print("Amount is can`t be draw or smaller than 0")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print("Withdraw succesed")
        elif amount > self._balance:
            print("Amount is bigger than balance")

    def transfer(self, other_accaunt, amount):
        if other_accaunt != self._accaunt_number:
            self._balance -= amount
            print("Transfer succesed")
        elif other_accaunt == self._accaunt_number:
            raise TypeError("You can't transfer money to yourself")

    def __str__(self):
        return f"Balance is: {self._balance}"

    def __repr__(self):
        return f"Balance is: {self._balance}"


class SavingsAccount(BankAccount):
    def __init__(self, owner, _balance, accaunt_number, balance_savings):
        self._owner = owner
        self._balance = _balance
        self._accaunt_number = accaunt_number
        self._savings = balance_savings

    def add_interest(self, interest_savings):
        self._savings += interest_savings
        print("Savings account added successfully")


class BusinessAccount(BankAccount):
    def __init__(self, owner, _balance, accaunt_number, credit_limit):
        self._owner = owner
        self._balance = _balance
        self._accaunt_number = accaunt_number
        self._credit_limit = credit_limit

    def withdraw_limit(self, amount):
        if amount < self._credit_limit and self._balance > amount:
            self._balance -= amount
            print("Withdraw succesed")
        else:
            print("You can't withdraw money")


bank1 = BankAccount("Alex", 1000, 78)
bank1.deposit(100)
print(bank1)
bank2 = BankAccount("Bob", 1000, 57)
bank2.withdraw(100)
print(bank2)
bank3 = SavingsAccount("Bob", 100, 10, 100)
bank3.add_interest(100)
print(bank3)
bank4 = BusinessAccount("George", 10000, 45, 100)
bank4.withdraw(1100)
bank4.withdraw_limit(90)
print(bank4)
