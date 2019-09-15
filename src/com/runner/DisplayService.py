from colorama import Fore, Style

board_rows = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
name_section_len_limit = 22
space_string = ' '


class DisplayService:

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.game_history = {player_1.name: 0, player_2.name: 0, 'tie': 0}

    def get_text_with_color(self, num, win_flag, game_board):
        if self.player_1.move_style == game_board[num]:
            if win_flag:
                return Fore.GREEN + game_board[num] + Style.RESET_ALL
            else:
                return self.player_1.color + game_board[num] + Style.RESET_ALL
        elif self.player_2.move_style == game_board[num]:
            if win_flag:
                return Fore.GREEN + game_board[num] + Style.RESET_ALL
            else:
                return self.player_2.color + game_board[num] + Style.RESET_ALL
        else:
            return Fore.YELLOW + game_board[num] + Style.RESET_ALL

    def print_board_row(self, row, game_board):
        num1, num2, num3 = row
        print('|       |       |       |')
        print(f'|   {self.get_text_with_color(num1, False, game_board)}   |'
              f'   {self.get_text_with_color(num2, False, game_board)}   '
              f'|   {self.get_text_with_color(num3, False, game_board)}   |')
        print('|_______|_______|_______|')

    def display_board(self, game_board):
        print(' _______________________')
        for row in board_rows:
            self.print_board_row(row, game_board)

    def show_game_result(self, winning_player, winning_row):
        if winning_player is None:
            self.game_history['draw'] += 1
            print(Fore.BLUE + 'Its a stalemate...' + Style.RESET_ALL)
        else:
            self.game_history[winning_player.name] += 1
            print(Fore.GREEN + f'{winning_player.name} wins this game !')
            print(f'winning tiles = {winning_row}' + Style.RESET_ALL)

    def display_final_score(self):
        print(' _____________________________________')
        print('|             FINAL SCORE             |')
        print('|_____________________________________|')
        for name in self.game_history:
            name_len_diff = 22 - len(name)
            if len(name) % 2 == 0:
                printable_name = (space_string * (name_len_diff // 2)) + name + \
                                 (space_string * (name_len_diff // 2))
            else:
                printable_name = (space_string * (name_len_diff // 2)) + name + (
                        space_string * (name_len_diff // 2)) + space_string

            score_len_diff = 14 - len(str(self.game_history[name]))
            if len(str(self.game_history[name])) % 2 == 0:
                printable_score = (space_string * (score_len_diff // 2)) + str(self.game_history[name]) \
                                  + (space_string * (score_len_diff // 2))
            else:
                printable_score = (space_string * (score_len_diff // 2)) + str(self.game_history[name]) \
                                  + (space_string * (score_len_diff // 2)) + space_string

            print(f'|{printable_name}|{printable_score}|')
        print('|______________________|______________|')
