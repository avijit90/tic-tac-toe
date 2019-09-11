import DisplayService
import UserInputService

user_moves_status = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

player_1, player_2 = UserInputService.create_players()
print(player_1)
print(player_2)

DisplayService.display_board(player_1, player_2, user_moves_status)
