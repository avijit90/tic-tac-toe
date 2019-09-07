starting_moves = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


class DisplayService:
    user_moves_status = []
    player_1 = None
    player_2 = None

    def __init__(self, player_1, player_2):
        self.user_moves_status = starting_moves
        self.player_1 = player_1
        self.player_2 = player_2
        pass

    def display_board(self):
        print('\033[1;30m _______________________')
        for row in [(1, 2, 3), (4, 5, 6), (7, 8, 9)]:
            self.print_board_row(row[0], row[1], row[2])

    def print_board_row(self, num1, num2, num3):
        print('\033[1;30m|       \033[1;30m|       \033[1;30m|       \033[1;30m|')
        print(
            f'\033[1;30m|   \033{self.get_text_with_color(num1, False)}   \033[1;30m|'
            f'   \033{self.get_text_with_color(num2, False)}   '
            f'\033[1;30m|   \033{self.get_text_with_color(num3, False)}   \033[1;30m|')
        print('\033[1;30m|_______|_______|_______|\033[0;30m')

    def get_text_with_color(self, num, win_flag):
        if self.player_1['style'] == self.user_moves_status[num]:
            if win_flag:
                return "[1:32m" + self.user_moves_status[num]
            else:
                return self.player_1['move_color'] + "m" + self.user_moves_status[num]
        elif self.player_2['style'] == self.user_moves_status[num]:
            if win_flag:
                return "[1:32m" + self.user_moves_status[num]
            else:
                return self.player_2['move_color'] + "m" + self.user_moves_status[num]
        else:
            return '[0;33m' + self.user_moves_status[num]
