# Let import he libraries we will be usig 
# in this case it will just be the UNIT TEST library 

import unittest
# Lets make a function that will be testing 
# Let's calculate how many treats our pet dragon will get based on his good deeds. 
def calculate_dragon_treats(good_deeds):
   # For each good deed our pet dragon does it will get 3 treats. 
   # Calculate the number of treats here
   result = good_deeds * 3
   
   # Now lets return the result back to the caller of this function.
   return result

   # Now for the fun part, we can write a testing group class that uses our library 
   # unittest that we imported over.
class TestDragonTreats(unittest.TestCase):
    # Now we can write a specific test case for our function 
    # This has a start with the word test_ so that the unittest library knows this is a test case function.
    def test_treat_calculation(self):
   
       # Now inside our test case function let use a standard 
       # assert function to check if our function is working correctly.
       # Here we pass in 2 good deeds and except to get 6 treats back since 2 * 3 = 6
       self.assertEqual(calculate_dragon_treats(2), 6)

# Our program will start here on this line 
if __name__ == '__main__':
    # Let's instruct the unittest library to run our tests.
    # This is not calling a main function we wrote.
    # This is calling a built in main function in our unit test library.
    unittest.main()
