from com.runner.Player import Player

violet = {'bold': '[1;35m', 'normal': '[0;35m'}
blue = {'bold': '[1;34m', 'normal': '[0;34m'}


def get_player_names():
    player_1_name_input = input("Player 1 - Please enter you name\n")
    player_2_name_input = input("Player 2 - Please enter you name\n")
    return player_1_name_input, player_2_name_input


def get_player_move_choice(player_1, player_2):
    input_styles = ['X', 'O']
    player_style_input = input(f"{player_1.name}, please pick a marker 'X' or 'O'\n")

    while player_style_input.upper() not in input_styles:
        print(f'\033[1;31mInvalid input : {player_style_input}\033[0;30m')
        player_style_input = input(
            f"{player_1.name}, please choose a marker only between \033[1;32m{input_styles[0]} "
            f"\033[0;30mor \033[1;32m{input_styles[1]}\033[0;30m\n")

    player1_choice = player_style_input.upper()
    input_styles.pop(input_styles.index(player_style_input.upper()))
    player2_choice = input_styles[0]

    player_1.move_style = player1_choice
    player_2.move_style = player2_choice


def create_players():
    player_1_name_input, player_2_name_input = get_player_names()
    player_1 = Player(player_1_name_input)
    player_2 = Player(player_2_name_input)
    get_player_move_choice(player_1, player_2)
    player_1.colorize_player(violet)
    player_2.colorize_player(blue)
    return player_1, player_2


