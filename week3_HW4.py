import unittest

from shopping import Cart

class Test_Cart(unittest.TestCase):

    def test_add(self):
        item = input('What item are you adding?').lower()
        self.Cart.add()
        result = Cart("How many items would you like to add?")
        quantity = input(f"How many {item} would you like to add?: ")
        self.assertEqual(len(Cart.grocery_dict)) == 1
        self.Cart.grocery_dict['bread']['quantity'] == 2
        self.Cart.grocery_dict['eggs']['price'] == 2.5
        expected_output = (result, f"You have {item} in the cart.")
        self.add()

    def test_remove(self):
        item_to_remove = input('What item would you like to remove?: ').lower()
        quantity = int(input('How many would you like to remove?: '))
        self.Cart.add()
        self.Cart.remove()
        self.assertLess(len(Cart.grocery_dict)) == 0
        self.Cart.grocery_dict['apples']['quantity'] == 3
        expected_output = (quantity, f"you have remove {item_to_remove} in the cart")

    def test_show(self):
        cart = Cart()
        self.Cart.add()
        self.Cart.show()
        assert Cart.grocery_dict == {'bread': {'quantity': 2, 'price': 2.5}}
        print("Thanks for shopping!")

if __name__ == '__main__':
    unittest.main()
