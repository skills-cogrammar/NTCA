from src.views.user_view import UserView
from src.views.challenge_view import ChallengeView

user_view = UserView()

if __name__ == '__main__':
    
    username = user_view.get_login_details()

    while (not username):
        username = user_view.get_login_details()

    challenge_view = ChallengeView(username)

    challenge_view.display_menu()