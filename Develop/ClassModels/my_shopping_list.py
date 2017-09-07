class ShoppingList:
    """This class models the creation of a shopping list"""

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.purchased_items = {}

    def add_item(self, item):
        """This method adds an  item into the shopping list dictionary"""
        self.purchased_items.update({item.name: item})

    def remove_item(self, item_name):
        """This method deletes an item from the shopping list"""
        self.purchased_items.pop(item_name)

    def update_list_item(self, item_name, item):
        """This method updates items on the shopping list"""
        self.purchased_items.pop(item_name)
        self.purchased_items.update({item_name.name: item})
