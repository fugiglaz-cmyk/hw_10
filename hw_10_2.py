class Product:
    def __init__(self, name: str, price: int, quantity: int, category: str):
        """
        Initializes a product object.

        Args:
            name (str): Product name.
            price (int): Product price.
            quantity (int): Product quantity.
            category (str): Product category.

        Returns:
            None: Initializes product attributes.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    @property
    def price(self):
        """
        Gets the product price.

        Args:
            None.

        Returns:
            int: Current product price.
        """
        return self._price

    @price.setter
    def price(self, value: int):
        """
        Sets the product price.

        Args:
            value (int): New product price.

        Returns:
            None: Updates product price.

        Raises:
            ValueError: If price is negative.
        """
        if value < 0:
            raise ValueError("Incorrect price")
        self._price = value

    @property
    def quantity(self):
        """
        Gets the product quantity.

        Args:
            None.

        Returns:
            int: Current product quantity.
        """
        return self._quantity

    @quantity.setter
    def quantity(self, value: int):
        """
        Sets the product quantity.

        Args:
            value (int): New product quantity.

        Returns:
            None: Updates product quantity.

        Raises:
            ValueError: If quantity is negative.
        """
        if value < 0:
            raise ValueError("Incorrect quantity")
        self._quantity = value

    @property
    def name(self):
        """
        Gets the product name.

        Args:
            None.

        Returns:
            str: Current product name.
        """
        return self._name

    @name.setter
    def name(self, value: str):
        """
        Sets the product name.

        Args:
            value (str): New product name.

        Returns:
            None: Updates product name.

        Raises:
            ValueError: If name is None or empty.
        """
        if not value:
            raise ValueError("Incorrect name")
        self._name = value

    def increase_stock(self, amount: int):
        """
        Increases product stock.

        Args:
            amount (int): Amount of products to add.

        Returns:
            None: Updates product quantity.
        """
        if amount > 0:
            self.quantity += amount

    def decrease_stock(self, amount: int):
        """
        Decreases product stock.

        Args:
            amount (int): Amount of products to remove.

        Returns:
            None: Updates product quantity.

        Raises:
            ValueError: If amount exceeds available stock.
        """
        if amount < 0 or amount > self.quantity:
            raise ValueError("Incorrect stock amount")
        self.quantity -= amount

    def calculate_total_value(self):
        """
        Calculates total value of products in stock.

        Args:
            None.

        Returns:
            int: Product price multiplied by quantity.
        """
        return self.quantity * self.price

    def __str__(self):
        """
        Returns a readable product representation.

        Args:
            None.

        Returns:
            str: Product name and price.
        """
        return f"Name: {self.name}, Price: {self.price}"

    def __repr__(self):
        """
        Returns a detailed product representation.

        Args:
            None.

        Returns:
            str: Product information.
        """
        return (
            f"Name: {self.name}, Price: {self.price}, "
            f"Quantity: {self.quantity}, Category: {self.category}"
        )

    def __eq__(self, other):
        """
        Compares two products by price.

        Args:
            other (Product): Another product.

        Returns:
            bool: True if prices are equal, otherwise False.
        """
        if not isinstance(other, Product):
            return NotImplemented
        return self.price == other.price

    def __lt__(self, other):
        """
        Compares two products by price.

        Args:
            other (Product): Another product.

        Returns:
            bool: True if current product is cheaper.
        """
        if not isinstance(other, Product):
            return NotImplemented
        return self.price < other.price

    def __add__(self, other):
        """
        Adds quantities of products in the same category.

        Args:
            other (Product): Another product.

        Returns:
            int: Sum of quantities if categories match.
            None: If categories are different.
        """
        if not isinstance(other, Product):
            return NotImplemented
        if self.category == other.category:
            return self.quantity + other.quantity
        return None

    def __mul__(self, number: int):
        """
        Multiplies product quantity by a number.

        Args:
            number (int): Multiplication factor.

        Returns:
            int: Result of multiplication.
        """
        return self.quantity * number


prod1 = Product(name="Milk", price=100, quantity=13, category="Dairy")
print(repr(prod1))
prod2 = Product(name="Butter", price=50, quantity=15, category="Dairy")
print(prod2)
print(prod1 + prod2)
print(prod1 * 4)
print(prod1 > prod2)
print(prod1 == prod2)
print(prod1.calculate_total_value())
