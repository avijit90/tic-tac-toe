from com.runner.DisplayService import DisplayService
from com.runner.UserInputService import UserInputService


def run_me():
    user = UserInputService()
    print(user.player_1)
    print(user.player_2)
    display = DisplayService(user.player_1, user.player_2)
    display.display_board()


run_me()
