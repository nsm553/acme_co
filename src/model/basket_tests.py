import unittest

from product import Product
from shipping_rule import ShippingRule
from bogo50_offer import BOGO50Offer
from catalog import Catalog
from basket import Basket

class BasketTests(unittest.TestCase):
    """ Test Class for unit testing """
    def setUp(self):
        catalog = Catalog()

        catalog.addShippingRule("U50", 50, 4.95)
        catalog.addShippingRule("U90", 90, 2.95)
        catalog.addShippingRule("U90", 90, 0)

        catalog.addOffer(BOGO50Offer("BOGO50", "R01"))

        catalog.addProduct(Product("R01", "Red Widget", 32.95))
        catalog.addProduct(Product("G01", "Green Widget", 24.95))
        catalog.addProduct(Product("B01", "Blue Widget", 7.95))

        self.basket = Basket(catalog)

    def test_case1(self):
        """
        Test Case 1
        """
        self.basket.addProduct("B01", 1)
        self.basket.addProduct("G01", 1)

        amt = self.basket.getFinalAmount("BOGO50")
        total = float(amt)
        self.assertEqual(total, 37.85)

    def test_case2(self):
        """
        Test Case 2
        """
        self.basket.addProduct("R01", 1)
        self.basket.addProduct("R01", 1)

        amt = self.basket.getFinalAmount("BOGO50")
        total = float(amt)
        self.assertEqual(total, 54.37)

    def test_case3(self):
        """
        Test Case 3
        """
        self.basket.addProduct("R01", 1)
        self.basket.addProduct("G01", 1)

        amt = self.basket.getFinalAmount("BOGO50")
        total = float(amt)
        self.assertEqual(total, 60.85)

    def test_case4(self):
        """
        Test Happy path
        """
        self.basket.addProduct("B01", 1)
        self.basket.addProduct("B01", 1)
        self.basket.addProduct("R01", 1)
        self.basket.addProduct("R01", 1)
        self.basket.addProduct("R01", 1)

        amt = self.basket.getFinalAmount("BOGO50")
        total = float(amt)
        self.assertEqual(total, 98.27)

    def test_invalid_coupon(self):
        """
        Test Validation
        """
        self.basket.addProduct("R01", 2)

        amt = self.basket.getFinalAmount("BOGO50000000000")
        total = float(amt)
        self.assertTrue(total, 68.85)

    def test_add_sub_items(self):
        """
        Test Add Remove Items
        """
        self.basket.addProduct("R01", 1)
        self.basket.removeProduct("R01", 1)

        total = self.basket.getFinalAmount("BOGO50")
        self.assertEqual(total, 0)

    def test_invalid_product(self):
        """
        Test Validation
        """
        self.basket.addProduct("TTT", 2)

        total = self.basket.getFinalAmount("BOGO50")
        self.assertRaises(ValueError("Product is not available"))

    def test_raise_err(self):
        """
        Test Validation
        """
        self.basket.addProduct("R01", -2)

        total = self.basket.getFinalAmount("BOGO50")
        self.assertTrue("Quantity can't be negative" in context.msg)

if __name__ == "__main__":
    unittest.main()

