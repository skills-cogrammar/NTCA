import unittest 
from src.services.user_service import UserService
from src.models.user_model import UserModel


class TestUserService(unittest.TestCase):

    def setUp(self) -> None:
        self.user_service = UserService()

    def test_login_valid_user(self):
        username = 'admin'
        password = 'admin'

        user =  UserModel(username, password)

        actual = self.user_service.login(user)

        expected = 'admin'
        self.assertEqual(actual, expected)

    

if __name__ == '__main__':
    unittest.main()