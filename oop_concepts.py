from abc import ABCMeta


class Product(object):
    """
    An abstract class
    """

    __metaclass__ = ABCMeta

    unit_price = 0

    def __init__(self, name, maker):
        self.__name = name
        self.__maker = maker
        self._quantity = 0
        self._total_stock_price = 0

    def add_stock(self, quantity):
        self._quantity += quantity
        self._total_stock_price += self.unit_price * quantity

    def sell(self, quantity):
        self._quantity -= quantity
        self._total_stock_price -= self.unit_price * quantity

    def get_name(self):
        """Demonstration of encapsulation; this is a wrapper to allow access to the value in __name"""
        return self.__name

    def check_product_catalogue(self):
        """A method to demonstrate polymorphism"""
        pass


class Phone(Product):
    """
    Implementing a phone class, which is a subclass 
    of the product class, to demonstrate inheritance
    """

    unit_price = 400

    def check_product_catalogue(self):
        return str(self._quantity) + " " + self.get_name() + " phones at " + str(Phone.unit_price) + "@, total: " + str(self._total_stock_price)


class China(Phone):
    """
    Similar to the Phone class
    """

    unit_price = 100

    def check_product_catalogue(self):
        """A demonstration of polymorphism"""
        return str(self._quantity) + " " + self.get_name() + " at " + str(China.unit_price) + "@, total: " + str(self._total_stock_price)


def main():
    product = Product("Corolla", "Toyota")

    phone = Phone("Samsung Galaxy S6 Edge", "Samsung")
    phone.add_stock(10)
    print(phone.check_product_catalogue())
    phone.sell(5)
    print(phone.check_product_catalogue())

    phone = China("Plates", "Nice house of plastics")
    phone.add_stock(12)
    print(phone.check_product_catalogue())
    phone.sell(6)
    print(phone.check_product_catalogue())


if __name__ == '__main__':
    main()