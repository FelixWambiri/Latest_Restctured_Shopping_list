class UsersAccountList:
    """This class is the model of wah actions/methods can be implemented on the  users"""

    def __init__(self):
        self.users_list = {}

    def create_users(self, user):
        """This method adds individual users to the overall user accounts list"""
        if user.username in self.users_list:
            raise KeyError
        else:
            self.users_list.update({user.username: user})

    def view_users(self, user_name):
        """This method can be used to view a particular user"""
        return self.users_list.get(user_name)

    def delete_users(self, user_name):
        """This method deletes a user from the dictionary"""
        self.users_list.pop(user_name)

    def update_users_list(self, user_name, user):
        """This method updates the details of the user"""
        self.users_list.pop(user_name)
        self.users_list.update({user.username: user})
