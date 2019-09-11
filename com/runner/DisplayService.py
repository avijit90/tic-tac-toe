board_rows = ((1, 2, 3), (4, 5, 6), (7, 8, 9))


def get_text_with_color(num, win_flag, player_1, player_2, user_moves_status):
    if player_1.move_style == user_moves_status[num]:
        if win_flag:
            return "[1:32m" + user_moves_status[num]
        else:
            return player_1.move_color + "m" + user_moves_status[num]
    elif player_2.move_style == user_moves_status[num]:
        if win_flag:
            return "[1:32m" + user_moves_status[num]
        else:
            return player_2.move_color + "m" + user_moves_status[num]
    else:
        return '[0;33m' + user_moves_status[num]


def print_board_row(row, player_1, player_2, user_moves_status):
    num1, num2, num3 = row
    print('\033[1;30m|       \033[1;30m|       \033[1;30m|       \033[1;30m|')
    print(
        f'\033[1;30m|   \033{get_text_with_color(num1, False, player_1, player_2, user_moves_status)}   \033[1;30m|'
        f'   \033{get_text_with_color(num2, False, player_1, player_2, user_moves_status)}   '
        f'\033[1;30m|   \033{get_text_with_color(num3, False, player_1, player_2, user_moves_status)}   \033[1;30m|')
    print('\033[1;30m|_______|_______|_______|\033[0;30m')


def display_board(player_1, player_2, user_moves_status):
    print('\033[1;30m _______________________')
    for row in board_rows:
        print_board_row(row, player_1, player_2, user_moves_status)
