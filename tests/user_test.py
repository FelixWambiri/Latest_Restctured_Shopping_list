import unittest

from Develop.ClassModels.my_shopping_list import ShoppingList
from Develop.ClassModels.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("felo", "felowambiri@gmail.com", "felo")
        self.myshoppinglist = ShoppingList("Dubai", "Shopping I performed of electricals when I went to dubai")

    def test_add_shopping_list(self):
        self.assertEqual(0, len(self.user.shopping_lists))
        self.user.create_shopping_list(self.myshoppinglist)
        self.assertEqual(1, len(self.user.shopping_lists))

    def test_del_shopping_list(self):
        self.assertEqual(0, len(self.user.shopping_lists))
        self.user.create_shopping_list(self.myshoppinglist)
        self.assertEqual(1, len(self.user.shopping_lists))
        self.user.delete_shopping_list(self.myshoppinglist.name)
        self.assertEqual(0, len(self.user.shopping_lists))





if __name__ == '__main__':
    unittest.main()
