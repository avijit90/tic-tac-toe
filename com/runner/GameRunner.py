import colorama

from DisplayService import DisplayService
from InputService import InputService
from ResultService import ResultService

colorama.init()
inputService = InputService()
player_1, player_2 = inputService.create_players()

print(player_1)
print(player_2)
print('Players successfully created !')

displayService = DisplayService(player_1, player_2)
displayService.display_board(inputService.game_board)

result_service = ResultService(player_1, player_2)
style_switch = True
while len(inputService.available_tiles) > 0:
    selected_player = player_1 if style_switch else player_2
    inputService.play_moves(selected_player)
    print('\n' * 10)
    displayService.display_board(inputService.game_board)
    result_service.check_winner(inputService.game_board)
    if result_service.win_evaluation_result:
        break
    style_switch = not style_switch

result_service.determine_winner(inputService.game_board)
displayService.show_game_result(result_service.winning_player)
