from product import Product

class BOGO50Offer(object):
    """ BuyOneGetOne 50 % Offer """

    def __init__(self, offer_code: str, product_code: str):
        """
        Initialize offer details, e.g. super("BOGO50", "R01")   
        can be list of product codes (future)
        """
        # super(offer_code, product_code)
        self.offer_code = offer_code
        self.product_code = product_code

    def discountedPrice(self, product: Product, qty: int) -> float:
        """
        :param  product
        :param  qty Number of product items

        return final amount considering the discount code
        """
        if product is None or product.code is None:
            raise ValueError ("Invalid product code")

        if self.product_code == product.code:
            f = (qty // 2) * product.price * 1.5 + ((qty%2) * product.price)
        else:
            f = product.price * qty

        return f
