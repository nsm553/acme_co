
class ShippingRule(object):
    """ Holds definition of a Shipping Rule"""

    def __init__(self, rule_id: str , min_amount: int, cost: float):
        """ Shipping Rule constructor based on tiered pricing
        sorted on min_amount to calculate range for total cost

        :param rule_id: Rule identifier
        :param min_amount:   Price limit for delivery cost
        :param cost:     Delivery Cost
        """
        self.rule_id = rule_id
        self.min_amount = min_amount
        self.cost = cost