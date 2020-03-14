
(project structure is not as planned due to a packaging and model import issues)

Model: 

Catalog-
Holds mostly pre-defined data like rules, offers, products, a good replaceement with external storage/DB

product-
Holds details of a product - code, price

offer-
Plan is to have an Offer interface with BOGO50Offer being a special implementation.
Each offer is initialized with an offer_code and list of products this offer shall be applicable 
discountedPrice - has the specifi logic to calculate and return price based on its internal math/logic
This should be able to take multiple products which are able to handle same coupon code
BOGO50Offer - is specific to buy one get one 50% off logic

rule-
ShippingRule Represents Shipping rule
Plan is to have a separate Shipping Manager to take in shipping rules and calculate shipping, but right now is put in Basket class itself, where all rules are sorted based on price and final shipping is calcualated.

Bucket-
Provides functionality to add/remove products, calcualte shiping (refactor later), delegates discount caluclation to respective offer class
Provides basic validation, whcih should be extended
getFinalAmount, returns the final amount considering discount and shipping rules.


Testing:
Started with testing as a different module, ran into module import issues, so is part of model package
Has the test cases listed, along with some additional negative testing