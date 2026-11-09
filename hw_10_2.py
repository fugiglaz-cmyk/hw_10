class Product:
    def __init__(self, name: str, price: str, quantity: str, category: str):
        """method for initialization"""
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    @property
    def price(self):
        """method for property"""
        return self._price

    @price.setter
    def price(self, value: None):
        """method for property setter"""
        if value < 0:
            raise ValueError("Incorrect price")
        self._price = value

    @property
    def quantity(self):
        """method for property"""
        return self._quantity

    @quantity.setter
    def quantity(self, value: None):
        """method for property setter"""
        if value < 0:
            raise ValueError("Incorrect quantity")
        self._quantity = value

    @property
    def name(self):
        """method for property"""
        return self._name

    @name.setter
    def name(self, value: None):
        """method for property setter"""
        if value == None:
            raise ValueError("Incorrect name")
        self._name = value

    def increase_stock(self, amount: int):
        """method for increase stock"""
        self.quantity += amount

    def decrease_stock(self, amount: int):
        """method for decrease stock"""
        self.quantity -= amount

    def calculate_total_value(self):
        """method for calculate total value"""
        return self.quantity * self.price

    def __str__(self):
        """method for string"""
        return f"Name: {self.name}, Price: {self.price}"

    def __repr__(self):
        """method for repr"""
        return f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Category: {self.category}"

    def __eq__(self, other: str):
        """method for equality"""
        return self.price == other.price

    def __lt__(self, other: str):
        """method for less than"""
        return self.price < other.price

    def __add__(self, other: str):
        """method for addition"""
        if self.category == other.category:
            return self.quantity + other.quantity

    def __mul__(self, number: int):
        """method for multiplication"""
        return self.quantity * number


prod1 = Product(name="Milk", price=100, quantity=13, category="Dairy")
print(repr(prod1))
prod2 = Product(name="Butter", price=50, quantity=15, category="Dairy")
print(prod2)
print(prod1 + prod2)
print(prod1 * 4)
print(prod1 > prod2)
print(prod1 == prod2)
