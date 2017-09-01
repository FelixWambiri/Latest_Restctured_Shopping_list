import unittest

from Develop.ClassModels.items import Item
from Develop.ClassModels.my_shopping_list import ShoppingList


class TestMyShoppingList(unittest.TestCase):
    def test_add_item(self):
        myshopinglist = ShoppingList("Somalia",
                                       "This is the shopping list of items i bought in somalia while on a trip there.")
        item = Item("Laptop", "80000", "2 pieces")
        self.assertEqual(0, len(myshopinglist.shopping_list))
        myshopinglist.add_item(item)

    def test_you_can_add_multiple_items(self):
        myshopinglist = ShoppingList("Somalia", "shopping list of items i bought in somalia.")
        item = Item("Laptop", "80000", "2 pieces")
        item2 = Item("Laptop2", "80000", "2 pieces")
        item3 = Item("Laptop3", "80000", "2 pieces")
        myshopinglist.add_item(item)
        myshopinglist.add_item(item2)
        myshopinglist.add_item(item3)
        self.assertEqual(3, len(myshopinglist.shopping_list))


if __name__ == '__main__':
    unittest.main()
