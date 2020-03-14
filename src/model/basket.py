from product import Product
from shipping_rule import ShippingRule
from bogo50_offer import BOGO50Offer
from catalog import Catalog

class Basket(object):
    """ Basket class - Main class to hold items and perform all calculations """
    catalog: Catalog

    def __init__(self, catalog: Catalog):
        """
        Initialize with a Catalog containing offers and ShippingRules
        products holds products
        """
        self.catalog = catalog
        self.products = dict()


    def addProduct(self, product_code: str, qty: int):
        """
        Add a Product and quantity
        """
        if self.catalog.products.get(product_code) is None:
            raise ValueError("Product is not available")
        if qty <= 0:
            raise ValueError("Quantity can't be negative")
        
        cur_qty = self.products.get(product_code, 0)
        self.products[product_code] = cur_qty + qty


    def removeProduct(self, product_code: str, qty: int):
        """
        Remove a Product with quantity
        """
        if self.catalog.products.get(product_code) is None:
            raise ValueError("Product is not available")

        cur_qty = self.products.get(product_code, 0)
        if cur_qty == 0:
            raise ValueError("Product was not added before")

        if cur_qty - qty < 0:
            raise ValueError("Can't reduce quantity below 0")
        if qty <= 0:
            raise ValueError("Quantity can't go negative")
        
        self.products[product_code] = cur_qty - qty


    def getFinalAmount(self, offer_code: str):
        amt = 0.0
        ''' calc discounted price for each product '''
        for k,v in self.products.items():
            product = self.catalog.products.get(k) 
            offer = self.catalog.offers.get(offer_code)
            if offer is not None:
                amt += offer.discountedPrice(product, v)
            else:
                print ("No offer found for this produt")
                amt += (product.price * v) 

        ''' in case add-remove and basket is empty'''
        if(amt == 0):
            return amt

        ''' calc shipping rate '''
        rules = sorted(self.catalog.rules, key=lambda rule: rule.min_amount)
        for rule in rules:
            if amt < rule.min_amount:
                amt += rule.cost
                break

        return amt // 0.01 / 100
