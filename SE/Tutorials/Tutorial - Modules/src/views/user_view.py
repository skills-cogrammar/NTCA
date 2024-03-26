import os

from src.controllers.user_controller import UserController
from src.models.user_model import UserModel


class UserView():

    def __init__(self) -> None:
        self.user_controller = UserController()

    def display_login_header(self):
        print('-'*10, 'LOGIN', '-'*10)

    def get_login_details(self):
        os.system('cls')

        self.display_login_header()

        username = input('Username: ')
        password = input('Password: ')

        user = UserModel(username, password)

        is_valid = self.user_controller.login(user)

        if not is_valid:
            print('Incorrect username or password')
            
        return is_valid

