import unittest

from Develop.ClassModels.items import Item
from Develop.ClassModels.my_shopping_list import ShoppingList


class TestMyShoppingList(unittest.TestCase):
    def setUp(self):
        self.myshoppinglist = ShoppingList("Somalia", "shopping list of items i bought in somalia.")
        self.item = Item("Laptop", "80000", "2 pieces")

    def test_add_item(self):
        self.assertEqual(0, len(self.myshoppinglist.purchased_items))
        self.myshoppinglist.add_item(self.item)

    def test_you_can_add_multiple_items(self):
        item = Item("Laptop", "80000", "2 pieces")
        item2 = Item("Laptop2", "80000", "2 pieces")
        item3 = Item("Laptop3", "80000", "2 pieces")
        self.myshoppinglist.add_item(item)
        self.myshoppinglist.add_item(item2)
        self.myshoppinglist.add_item(item3)
        self.assertEqual(3, len(self.myshoppinglist.purchased_items))

    def test_remove_item(self):
        self.myshoppinglist.add_item(self.item)
        self.assertEqual(1, len(self.myshoppinglist.purchased_items))
        self.myshoppinglist.remove_item(self.item.name)
        self.assertEqual(0, len(self.myshoppinglist.purchased_items))

    def test_an_exception_is_raised_when_a_user_tries_to_add_items_that_already_exist(self):
        self.myshoppinglist.add_item(self.item)
        with self.assertRaises(KeyError):
            self.myshoppinglist.add_item(self.item)

    def test_raises_an_exception_if_user_tries_to_delete_item_not_in_existence(self):
        with self.assertRaises(KeyError):
            self.myshoppinglist.remove_item(self.item.name)

    """def test_update_method_works(self):
        self.myshoppinglist.add_item(self.item)
        self.myshoppinglist.update_list_item(self.item.name, Item("Laptop", "800000", 2))
        self.assertEqual(2,self.item.quantity)"""


if __name__ == '__main__':
    unittest.main()
