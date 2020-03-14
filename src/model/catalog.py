from product import Product
from shipping_rule import ShippingRule
from bogo50_offer import BOGO50Offer

class Catalog(object):
    """ 
    Catalog contains all data, shall be replaced by DB/Storage
    List of ShippingRules [ShippingRule]
    Dict of Offers <offer_code, Offer>
    Dict of all offered Products
    """
    def __init__(self):
        """
        """    
        self.rules = list()
        self.offers = dict()
        self.products = dict()

    def addShippingRule(self, rule_id: str , min_amount: int, cost: float):
        self.rules.append(ShippingRule(rule_id, min_amount, cost))

    def addOffer(self, offer: BOGO50Offer):
        self.offers[offer.offer_code] = offer

    def addProduct(self, product: Product):
        """
        Add a Product
        """
        self.products[product.code] = product  

