
class Product(object):
    """ Represents a Product with price value """
    code: str
    name: str
    price: float

    def __init__(self, code: str, name: str, price: float):
        """
            Product definition
            :param code: product id
            :param name: Product Name
            :param price: price per unit   
        """
        self.code = code
        self.name = name
        self.price = price
    