import Offer
import Product

class Offer(object):

    def __init__(self, offer_code: str, product_code: str):
        """ Represents an Offer, discount calculation is modeled by sub classes

        :param offer_code: Offer code    
        :param  product_code:   Product this offer is elligible  (can be multiple products, simplifying to 1 for now)
        """
        self.offer_code = offer_code
        self.product_code = product_code

    def getDiscountedAmount(product: Product, qty: int) -> float:
        """
        Abstract method
        """
        pass