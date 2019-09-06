winning_combinations = ((1, 2, 3), (1, 4, 7), (1, 5, 9), (2, 5, 8), (3, 6, 9), (3, 5, 7), (4, 5, 6), (7, 8, 9))
winning_row = []
user_moves_status = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player_1 = {'move_color': '[1;35', 'info_color': '[0;35m'}
player_2 = {'move_color': '[1;34', 'info_color': '[0;34m'}
player_selected_styles = [player_1, player_2]
allowed_input_styles = ['X', 'O']
available_tiles = list(range(1, 10))
game_result = ''


def get_player_styles():
    input_styles = allowed_input_styles[:]
    player_style_input = input("Please pick a marker 'X' or 'O'\n")

    while player_style_input.upper() not in input_styles:
        print(f'\033[1;31mInvalid input : {player_style_input}\033[0;30m')
        player_style_input = input(f"Please choose a marker between \033[1;32m{input_styles[0]} "
                                   f"\033[0;30mor \033[1;32m{input_styles[1]}\033[0;30m\n")

    player1_choice = player_style_input.upper()
    input_styles.pop(input_styles.index(player_style_input.upper()))
    player2_choice = input_styles[0]
    player_1['style'] = player1_choice
    player_2['style'] = player2_choice


def display_board():
    print('\033[1;30m _______________________')
    for row in [(1, 2, 3), (4, 5, 6), (7, 8, 9)]:
        print_board_row(row[0], row[1], row[2])


def check_for_winning_combo(num, combo):
    return get_text_with_color(num, True) if num in combo else get_text_with_color(num, False)


def print_board_row(num1, num2, num3):
    print('\033[1;30m|       \033[1;30m|       \033[1;30m|       \033[1;30m|')
    print(
        f'\033[1;30m|   \033{get_text_with_color(num1, False)}   \033[1;30m|'
        f'   \033{get_text_with_color(num2, False)}   '
        f'\033[1;30m|   \033{get_text_with_color(num3, False)}   \033[1;30m|')
    print('\033[1;30m|_______|_______|_______|\033[0;30m')


def get_text_with_color(num, win_flag):
    if player_1['style'] == user_moves_status[num]:
        if win_flag:
            return "[1:32m" + user_moves_status[num]
        else:
            return player_1['move_color'] + "m" + user_moves_status[num]
    elif player_2['style'] == user_moves_status[num]:
        if win_flag:
            return "[1:32m" + user_moves_status[num]
        else:
            return player_2['move_color'] + "m" + user_moves_status[num]
    else:
        return '[0;33m' + user_moves_status[num]


def play_moves(selected_player):
    player_tile_input = input(f'\033{selected_player["info_color"]} Please choose a tile to play.\033[0;30m \n')

    while not player_tile_input.isdigit() or int(player_tile_input) not in available_tiles:
        print(f'\033[1;31mInvalid input : {player_tile_input}\033[0;30m')
        player_tile_input = input(
            f'Please choose a tile to play among values : \033[1;33m{available_tiles} \033[0;30m\n')

    print(f'Player Tile input is : {player_tile_input}')
    user_moves_status[int(player_tile_input)] = player_selected_styles[player_selected_styles.index(selected_player)][
        'style']
    available_tiles.pop(available_tiles.index(int(player_tile_input)))
    print('\n' * 10)
    display_board()


def run_game():
    style_switch = True
    while len(available_tiles) > 0:
        index = player_1 if style_switch else player_2
        play_moves(index)
        style_switch = not style_switch
        if check_winner():
            break

    if check_winner() is True:
        print('\n' * 10)
        print('\033[0;32mWe have a winner !\033[0;30m')
        display_winning_board()
    else:
        print('Its a stalemate...')


def check_winner():
    for combo in winning_combinations:
        if user_moves_status[combo[0]] != ' ' and user_moves_status[combo[0]] == user_moves_status[combo[1]] == \
                user_moves_status[combo[2]]:
            for value in combo:
                if value not in winning_row:
                    winning_row.append(value)
            return True

    return False


def display_winning_board():
    print('\033[1;30m _______________________')
    for row in [(1, 2, 3), (4, 5, 6), (7, 8, 9)]:
        print('\033[1;30m|       \033[1;30m|       \033[1;30m|       \033[1;30m|')
        print(
            f'\033[1;30m|   \033{check_for_winning_combo(row[0], winning_row)}   \033[1;30m|'
            f'   \033{check_for_winning_combo(row[1], winning_row)}   '
            f'\033[1;30m|   \033{check_for_winning_combo(row[2], winning_row)}   \033[1;30m|')
        print('\033[1;30m|_______|_______|_______|\033[0;30m')


get_player_styles()
print(f'\033{player_1["info_color"]}Player 1 has chosen : {player_1["style"]}\033[0;30m')
print(f'\033{player_2["info_color"]}Player 2 has been assigned : {player_2["style"]}\033[0;30m')
display_board()
run_game()
