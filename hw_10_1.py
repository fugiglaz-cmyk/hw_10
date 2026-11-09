class BankAccount:
    def __init__(self, owner: str, _balance: int, accaunt_number: int):
        """method for initialization"""
        self._owner = owner
        self._balance = _balance
        self._accaunt_number = accaunt_number

    def deposit(self, amount: int):
        """method for deposit"""
        if amount > 0:
            self._balance += amount
        elif amount <= 0:
            print("Amount is can`t be draw or smaller than 0")

    def withdraw(self, amount: int):
        """method for withdraws"""
        if amount <= self._balance:
            self._balance -= amount
            print("Withdraw succesed")
        elif amount > self._balance:
            print("Amount is bigger than balance")

    def transfer(self, other_accaunt: int, amount: int):
        """method for transfers"""
        if other_accaunt != self._accaunt_number:
            self._balance -= amount
            print("Transfer succesed")
        elif other_accaunt == self._accaunt_number:
            raise TypeError("You can't transfer money to yourself")

    def __str__(self):
        """method for printing"""
        return f"Balance is: {self._balance}"

    def __repr__(self):
        """method for representation"""
        return f"Balance is: {self._balance}"


class SavingsAccount(BankAccount):
    def __init__(self, owner: str, _balance: int, accaunt_number: int, balance_savings: int):
        """method for initialization"""
        self._owner = owner
        self._balance = _balance
        self._accaunt_number = accaunt_number
        self._savings = balance_savings

    def add_interest(self, interest_savings: int):
        """method for adding interest"""
        self._savings += interest_savings
        print("Savings account added successfully")


class BusinessAccount(BankAccount):
    def __init__(self, owner: str, _balance: int, accaunt_number: int, credit_limit: int):
        """method for initialization"""
        self._owner = owner
        self._balance = _balance
        self._accaunt_number = accaunt_number
        self._credit_limit = credit_limit

    def withdraw_limit(self, amount: int):
        """method for withdraw with limit"""
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
