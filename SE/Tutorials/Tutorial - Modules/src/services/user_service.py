from src.models.user_model import UserModel
from src.repositories.file_access_repo import FileAccessRepo
from constants import Constants


class UserService():    
    def __init__(self) -> None:
        self.__file_access = FileAccessRepo(Constants.USER_FILE_LOCATION)

    def login(self, user_details: UserModel) -> str:
        '''
        Check if the users login detalis are valid

        Args: 
            user_details: UserModel = login details for the user

        Returns:
            None - If the user details are invalid 
            Username - if the user details are valid
        '''
        existing_users = self.__file_access.read()

        for user in existing_users:
            username, password = user.split(';')

            if (username.strip() == user_details.username 
                and password.strip() == user_details.password):

                return user_details.username
            
        return None
