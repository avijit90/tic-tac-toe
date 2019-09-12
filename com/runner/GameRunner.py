import colorama

from DisplayService import DisplayService
from InputService import InputService
from ResultService import ResultService


def run_game():
    display_service = DisplayService(player_1, player_2)
    display_service.display_board(input_service.game_board)

    result_service = ResultService(player_1, player_2)
    style_switch = True
    while len(input_service.available_tiles) > 0:
        selected_player = player_1 if style_switch else player_2
        input_service.play_moves(selected_player)
        print('\n' * 10)
        display_service.display_board(input_service.game_board)
        result_service.check_winner(input_service.game_board)
        if result_service.win_evaluation_result:
            break
        style_switch = not style_switch

    result_service.determine_winner(input_service.game_board)
    display_service.show_game_result(result_service.winning_player, result_service.winning_row, game_history)

    return input_service.ask_play_again()


colorama.init()
input_service = InputService()
player_1, player_2 = input_service.create_players()
game_history = {player_1.name: 0, player_2.name: 0, 'tie': 0}
while True:
    play_again = run_game()
    if play_again.upper() == 'N':
        print('Game ends.. Bye !')
        print(game_history)
        break
    else:
        print('\n' * 10)
        input_service.reset_board()
