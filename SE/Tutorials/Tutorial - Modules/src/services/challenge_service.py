from datetime import datetime
from src.repositories.file_access_repo import FileAccessRepo
from src.models.challenge_model import ChallengeModel
from constants import Constants


class ChallengeService():
    def __init__(self):
        self.__file_repo = FileAccessRepo(Constants.CHALLENGES_FILE_LOCATION)

        self.__all_challenges: list[ChallengeModel] = []

        for challenge in self.__file_repo.read():
            self.__all_challenges.append(
                self.__convert_line_to_challenge_objects(challenge))

    def __convert_line_to_challenge_objects(self, line: str) -> ChallengeModel:
        line = tuple(line.split(';'))
        return ChallengeModel(*line)

    def get_mine(self, username: str) -> list:
        output = []

        for challenge in self.__all_challenges:
            if challenge.challenger == username:
                output.append(challenge)

        return output

    
    def get_all(self) -> list:
        return self.__all_challenges
    
    def get_all_challenges_received(self, username):
        output = []

        for challenge in self.__all_challenges:
            if challenge.challenging == username:
                output.append(challenge)

        return output
    
    def create_new_challenge(self, username: str, challenge_name: str,  
                             rules: str, challenging: str, deadline: str):
        # get the date string of the current date
        created_on = datetime.now().strftime("%Y-%m-%d")

        challenge = ChallengeModel(username, challenge_name, rules, challenging, created_on, deadline, None, None)

        self.__all_challenges.append(challenge)

        data = [value.date_to_string() for value in self.__all_challenges]

        self.__file_repo.write(data)



