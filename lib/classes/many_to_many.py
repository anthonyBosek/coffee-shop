class Coffee:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property  # getter
    def name(self):
        return self._name

    @name.setter  # setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Coffee name must be of type String.")
        elif len(new_name) < 3:
            raise ValueError("Coffee name must be between at least 3 characters.")
        elif hasattr(self, "name"):
            raise AttributeError("Coffee name cannot be change after initialization.")
        else:
            self._name = new_name

    def orders(self):
        return [order for order in Order.all if order.coffee is self]

    def customers(self):
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        prices = [order.price for order in self.orders()]
        return sum(prices) / len(prices) if len(prices) else 0
        # if len(prices):
        #     return sum(prices) / len(prices)
        # else:
        #     return 0


class Customer:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property  # getter
    def name(self):
        return self._name

    @name.setter  # setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Customer name must be of type String.")
        elif not 1 <= len(new_name) <= 15:
            raise ValueError("Customer name must be between 1 - 15 characters.")
        else:
            self._name = new_name

    def orders(self):
        return [order for order in Order.all if order.customer is self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        return Order(self, coffee, price)
        # maybe something here?? ( associates it with that customer and the coffee object provided)


class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        type(self).all.append(self)

    @property  # getter
    def customer(self):
        return self._customer

    @customer.setter  # setter
    def customer(self, new_cust):
        if not isinstance(new_cust, Customer):
            raise TypeError("Customer must be of type Customer class.")
        else:
            self._customer = new_cust

    @property  # getter
    def coffee(self):
        return self._coffee

    @coffee.setter  # setter
    def coffee(self, new_coff):
        if not isinstance(new_coff, Coffee):
            raise TypeError("Coffee must be of type Coffee class.")
        else:
            self._coffee = new_coff

    @property  # getter
    def price(self):
        return self._price

    @price.setter  # setter
    def price(self, new_price):
        if not isinstance(new_price, float):
            raise TypeError("Price must be of type float.")
        elif not 1.0 <= new_price <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0.")
        elif hasattr(self, "price"):
            raise AttributeError("Price cannot be change after initialization.")
        else:
            self._price = new_price
