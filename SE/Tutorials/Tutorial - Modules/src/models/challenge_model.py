from datetime import datetime


class ChallengeModel():
    def __init__(self, challenger: str, name: str, rules: str, challenging: str,
                 created_on: str, deadline: str, accepted: bool, winner: str) -> None:
        
        self.challenger = challenger
        self.name = name
        self.rules = rules
        self.challenging = challenging
        self.created_on = self.__convert_string_to_date(created_on)
        self.deadline = self.__convert_string_to_date(deadline)
        self.accepted = self.__set_string_to_none(accepted)
        self.winner = self.__set_string_to_none(winner)

    def __convert_string_to_date(self, date_string: str) -> datetime:
        return datetime.strptime(date_string, "%Y-%m-%d")
    
    def __set_string_to_none(self, string: str) -> str:
        if string == "None":
            return None
        return string

    def update_overdue(self):
        # Check if the deadline has passed and there is no winner 
        if self.deadline < datetime.now() and self.winner is None:
            self.winner = "Overdue"

    def date_to_string(self, date):
        return date.strftime("%Y-%m-%d")        

    def is_overdue(self):
        return self.winner == "Overdue"

    def accept_challenge(self):
        self.accepted = True

    def reject_challenge(self):
        self.accepted = False

    def set_winner(self, isChallenger: bool):
        if isChallenger:
            self.winner = self.challenger
        else:
            self.winner = self.challenging
    
    def __str__(self) -> str:
        return '\n'.join([
            f"Challenger: \t\t\t{self.challenger}",
            f"Challenge name: \t\t\t{self.name}",
            f"Rules: \t\t\t{self.rules}",
            f"Challenging: \t\t\t{self.challenging}",
            f"Created on: \t\t\t{self.created_on}",
            f"Deadline: \t\t\t{self.deadline}",
            f"Accepted: \t\t\t{self.accepted}",
            f"Winner: \t\t\t{self.winner}"
        ])
    
    def file_fortmat(self):
        return ';'.join([
            self.challenger,
            self.name,
            self.rules,
            self.challenging,
            self.date_to_string(self.created_on),
            self.date_to_string(self.deadline),
            self.accepted,
            self.winner
        ])