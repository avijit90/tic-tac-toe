import colorama

from DisplayService import DisplayService
from InputService import InputService
from ResultService import ResultService


class GameRunner:

    def __init__(self, input_service, display_service, player_1, player_2):
        self.input_service = input_service
        self.display_service = display_service
        self.player_1 = player_1
        self.player_2 = player_2

    def play_current_round(self):
        result_service = ResultService(self.player_1, self.player_2)
        style_switch = True
        while len(self.input_service.available_tiles) > 0:
            selected_player = self.player_1 if style_switch else self.player_2
            self.input_service.play_moves(selected_player)
            print('\n' * 10)
            self.display_service.display_board(self.input_service.game_board)
            result_service.check_winner(self.input_service.game_board)
            if result_service.win_evaluation_result:
                break
            style_switch = not style_switch

        result_service.determine_winner(self.input_service.game_board)
        self.display_service.show_game_result(result_service.winning_player, result_service.winning_row)

    def run_game(self):
        self.display_service.display_board(self.input_service.game_board)
        while True:
            self.play_current_round()
            play_again = self.input_service.ask_play_again()
            if play_again.upper() == 'N':
                print('Game ends.. Bye !')
                self.display_service.display_final_score()
                break
            else:
                print('\n' * 10)
                self.input_service.reset_board()
                self.display_service.display_board(self.input_service.game_board)


def execute():
    colorama.init()
    input_service = InputService()
    player_1, player_2 = input_service.create_players()
    display_service = DisplayService(player_1, player_2)
    game_runner = GameRunner(input_service, display_service, player_1, player_2)
    game_runner.run_game()


if __name__ == '__main__':
    execute()
