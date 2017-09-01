class User(object):
    """This class is the model of how the user object will be created with attributes and methods of the user"""
    """The init method below initialises the key attributes"""

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.shopping_lists = {}

    def create_shopping_list(self, list_item):
        """This method adds individual shopping lists into a dictionary which stores all the shopping lists created"""
        self.shopping_lists.update({list_item.name: list_item})

    def view_shopping_list(self, list_name):
        """This method displays an individual shopping list in the dictionary by using the name as the key"""
        return self.shopping_lists[list_name]

    def delete_shopping_list(self, list_name):
        """The method below deletes a particular shopping list in dictionary"""
        self.shopping_lists.pop(list_name)
