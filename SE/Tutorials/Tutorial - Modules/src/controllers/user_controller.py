from src.models.user_model import UserModel
from src.services.user_service import UserService


class UserController:
    '''
    Handles interactions with out user service and user UI
    '''

    def __init__(self) -> None:
        self.__user_service = UserService()

    def login(self, user_details: UserModel):
        '''
            Checks i the user credenails are correct 

            Args: 
                user_details: UserModel = the users details to be checked

            Returns:
                Username - if user is valid 
                None - if user is invalid
        '''
        return self.__user_service.login(user_details)
