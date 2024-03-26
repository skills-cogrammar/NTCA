from src.models.challenge_model import ChallengeModel
from src.services.challenge_service import ChallengeService


class ChallengeController():
    '''
    write what you need to write
    '''
    
    def __init__(self):
        self.challenge_service = ChallengeService()

    def get_mine(self, username: str) -> list:
        return self.challenge_service.get_mine(username)
    
    def create_challenge(self, username: str, challenge_name: str, rules: str, challenging: str, deadline: str):
        self.challenge_service.create_new_challenge(username, challenge_name, rules, challenging, deadline)

    def get_all(self):
        return self.challenge_service.get_all_challenges()
    
    def get_all_received(self, username: str):
        return self.challenge_service.get_all_challenges_received(username)
