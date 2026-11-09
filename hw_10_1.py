class BankAccount:
    def __init__(self, owner: str, _balance: int, accaunt_number: int):
        """
        Initializes a bank account.

        Args:
            owner (str): Account owner's name.
            _balance (int): Initial account balance.
            accaunt_number (int): Unique account number.

        Returns:
            None: Initializes the bank account attributes.
        """
        self._owner = owner
        self._balance = _balance
        self._accaunt_number = accaunt_number

    def deposit(self, amount: int):
        """
        Deposits money into the bank account.

        Args:
            amount (int): Amount of money to deposit.

        Returns:
            None: Updates the account balance or prints an error message.
        """
        if amount > 0:
            self._balance += amount
        elif amount <= 0:
            print("Amount is can't be draw or smaller than 0")

    def withdraw(self, amount: int):
        """
        Withdraws money from the bank account.

        Args:
            amount (int): Amount of money to withdraw.

        Returns:
            None: Updates the account balance or prints an error message.
        """
        if amount <= self._balance:
            self._balance -= amount
            print("Withdraw succesed")
        elif amount > self._balance:
            print("Amount is bigger than balance")

    def transfer(self, other_accaunt: int, amount: int):
        """
        Transfers money to another bank account.

        Args:
            other_accaunt (int): Account number of the recipient.
            amount (int): Amount of money to transfer.

        Returns:
            None: Updates the account balance or raises a TypeError
            if the recipient is the same account.
        """
        if other_accaunt != self._accaunt_number:
            self._balance -= amount
            print("Transfer succesed")
        elif other_accaunt == self._accaunt_number:
            raise TypeError("You can't transfer money to yourself")

    def __str__(self):
        """
        Returns a readable string representation of the bank account.

        Args:
            None.

        Returns:
            str: A string containing the current account balance.
        """
        return f"Balance is: {self._balance}"

    def __repr__(self):
        """
        Returns a string representation of the bank account.

        Args:
            None.

        Returns:
            str: A string containing the current account balance.
        """
        return f"Balance is: {self._balance}"


class SavingsAccount(BankAccount):
    def __init__(self, owner: str, _balance: int, accaunt_number: int, balance_savings: int):
        """
        Initializes a savings account.

        Args:
            owner (str): Account owner's name.
            _balance (int): Initial main account balance.
            accaunt_number (int): Unique account number.
            balance_savings (int): Initial savings balance.

        Returns:
            None: Initializes the savings account attributes.
        """
        self._owner = owner
        self._balance = _balance
        self._accaunt_number = accaunt_number
        self._savings = balance_savings

    def add_interest(self, interest_savings: int):
        """
        Adds interest to the savings balance.

        Args:
            interest_savings (int): Amount of interest to add.

        Returns:
            None: Updates the savings balance and prints a success message.
        """
        self._savings += interest_savings
        print("Savings account added successfully")


class BusinessAccount(BankAccount):
    def __init__(self, owner: str, _balance: int, accaunt_number: int, credit_limit: int):
        """
        Initializes a business bank account.

        Args:
            owner (str): Account owner's name.
            _balance (int): Initial account balance.
            accaunt_number (int): Unique account number.
            credit_limit (int): Maximum permitted credit limit.

        Returns:
            None: Initializes the business account attributes.
        """
        self._owner = owner
        self._balance = _balance
        self._accaunt_number = accaunt_number
        self._credit_limit = credit_limit

    def withdraw_limit(self, amount: int):
        """
        Withdraws money considering the credit limit.

        Args:
            amount (int): Amount of money to withdraw.

        Returns:
            None: Updates the account balance if withdrawal conditions
            are met; otherwise, prints an error message.
        """
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
