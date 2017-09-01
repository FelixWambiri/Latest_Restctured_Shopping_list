class ShoppingList:
    """This class models the creation of a shopping list"""

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.shopping_list = {}

    def add_item(self, item):
        """This method adds an  item into the shopping list dictionary"""
        self.shopping_list.update({item.name: item})

    def remove_item(self, item_name):
        """This method deletes an item from the shopping list"""
        self.shopping_list.pop(item_name)

    def update_list_item(self, item_name, item):
        """This method updates items on the shopping list"""
        """self.shopping_list[item_name] = self.shopping_list[new_item_name]"""
        """del self.shopping_list[item_name]"""
        """self.shopping_list[item_name] = new_items"""
        self.shopping_list.pop(item_name)
        self.shopping_list.update({item_name.name: item})
