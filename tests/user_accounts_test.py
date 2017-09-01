import unittest

from Develop.ClassModels.user import User
from Develop.ClassModels.user_accounts import UsersAccountList


class TestUserAccounts(unittest.TestCase):
    def test_if_tried_to_delete_account_that_does_not_exist_returns_error(self):
        usersaccountlist = UsersAccountList()
        with self.assertRaises(KeyError):
            usersaccountlist.delete_users("felix")

    def test_if_user_name_is_already_taken_person_should_use_another_user_name(self):
        usersaccountlist = UsersAccountList()
        user1 = User("felix", "felixwambiri@gmail.com", "feloh")
        usersaccountlist.create_users(user1)
        with self.assertRaises(KeyError):
            user2 = User("felix", "felixwambiri@gmail.com", "feloh")
            usersaccountlist.create_users(user2)

if __name__ == '__main__':
    unittest.main()