from src.models.challenge_model import ChallengeModel
from src.controllers.challenge_controller import ChallengeController

class ChallengeView():
    def __init__(self, username: str) -> None:
        self.__challenge_controller = ChallengeController()
        self.__username = username

    def display_menu(self):
        if (self.__username == 'admin'):
            self.admin_menu()
        else:
            self.general_user_menu()        

    def admin_menu(self):
        print('\n'.join([
            '1. Register Challenger',
            '2. Generate Report',            
            '3. View Challenges'
        ]))

    def general_user_menu(self):        
        print( '\n'.join([
            '1. View My Challenges',
            '2. View Challenges made to me',
            '3. Create new challenge'
            
        ]))

        self.general_user_choice()

    def general_user_choice(self):
        choice = input('-> ')

        if (choice == '1'):
            self.display_challenges(
                self.__challenge_controller.get_mine(self.__username))
        elif (choice == '2'):
            self.display_challenges(
                self.__challenge_controller.get_all_received(self.__username)
            )
        elif (choice == '3'):
            self.__create_challenge()
        else:
            print('Invalid choice')
            self.general_user_choice()

    def __create_challenge(self):
        challenge_name = input('Challenge Name: ')
        rules = input('Rules: ')
        challenging = input('Challenging: ')
        deadline = input('Deadline: ')

        self.__challenge_controller.create_challenge(self.__username, challenge_name, 
                                                     rules, challenging, deadline)

    def display_challenges(self, challenges: list[ChallengeModel]):
        for challenge in challenges:
            print(challenge)   
            print('-'*50)   

    


