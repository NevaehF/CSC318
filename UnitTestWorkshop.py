
# First we need to import the unit test library 
import unittest

""" 
This needs to be able to define a function that can calculate the final price after the disccount is applied 
    This will have 2 types of input: 
        The original price of the item
        The discount percentage that will be applied to the original price
"""
def calculate_discount(price, discount_percent):
    
    """
    Now we need to calculate the final price after the discount is applied
    First we need to make sure the price isn't negative since a negative price would't make sense nor will it work 
    we need to raise an error so it is able to signal an invalid input 
    """
    if price < 0:
        raise ValueError("Price can't be a negative amount")

    # Now we have to make sure the discount percentage is between 0 and 100 since a discount percentage outside of that range would not make sense 
    # If it is "Invalid Discount" needs to show
    if discount_percent < 0 or discount_percent > 100:
     raise ValueError("Discount must be between 0% and 100%")

    # If inputs are valid numbers, the discount price can be calculated 
    #price x (1 - discount_percent/100).
    return price * (1 - discount_percent / 100)

# Now we can make a test class that will inherit from discountunittest. TestCase
# This class will group tothether all of the cases for the function 
class TestDiscountCalculation(unittest.TestCase):
    
    # Test 1:  is the normal case
    # This will apply automatically apply 20% to $120. This should come back as 112 
    def test_normal_discount(self):
        self.assertEqual(calculate_discount(140, 20), 112)
    
    # Test 2: is going to be the Edge Case 
    # This test will apply a 0% discount to $30. This shouldn't change so it will come back as $30
    def test_zero_discount(self):
        self.assertEqual(calculate_discount(30, 0), 30)
        
    # Test 3: is going to also be an Edge Case 
    # This test is going to apply a 100% disccount to $84 and it should come back as $0 / Free 
    def test_full_discount(self):
        self.assertEqual(calculate_discount(75, 100), 0)
        
    # Test 4: This is going to test the Invalid Input return
    # Needs a negative price and it should return a ValueError
    def test_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_discount(-10, 10)
            
    # Test 5: Invalid input 
    # This needs to be a greater discount greater than 100%. This should also raise a ValueError 
    def test_invalid_dicount_percent(self):
        with self.assertRaises(ValueError):
            calculate_discount(100,150)
            
"""
Our program will start here on this line. 
unittest.main() will automatically find all test methods and execute them and report the results  
"""
if __name__ == '__main__':
    unittest.main()

